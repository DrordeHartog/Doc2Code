from docx import Document
import re
import yaml
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googletrans import Translator


def authenticate_google_drive(credentials_file):
    # Authenticate and create a Google Drive service instance
    credentials = service_account.Credentials.from_service_account_file(credentials_file, [
        "https://www.googleapis.com/auth/drive.readonly"])

    drive_service = build("drive", "v3", credentials=credentials)
    return drive_service


def download_file_from_drive(drive_service, file_id, destination):
    request = drive_service.files().get_media(fileId=file_id)
    fh = open(destination, "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()


def extract_sql_queries_from_docx(doc_file, sql_file):
    # Load the .docx file
    doc = Document(doc_file)

    # Open the .sql file in write mode
    with open(sql_file, 'w') as f:
        # Regular expression pattern to match SQL queries
        sql_pattern = re.compile(r"\b(SELECT|INSERT|UPDATE|DELETE|WITH|MERGE|ALTER|CREATE|DROP|TRUNCATE)\b",
                                 re.IGNORECASE)

        # Iterate over paragraphs in the document
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            match = sql_pattern.search(text)
            if match:
                f.write(text)
                f.write(";\n")

    print(f"SQL queries extracted and saved to {sql_file}")


def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='he', dest='en')
    return translation.text


def process_google_drive_folder(drive_service, folder_id, project_id):
    # Retrieve files in the specified Google Drive folder
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id, name)"
    ).execute()
    files = results.get('files', [])

    for file in files:
        file_id = file['id']
        file_name = file['name']
        translated_name = translate_to_english(file_name)
        doc_file = f"{file_id}.docx"
        sql_file = f"{translated_name}.sql"

        # Download the file from Google Drive
        download_file_from_drive(drive_service, file_id, doc_file)

        # Extract SQL queries and save to .sql file
        extract_sql_queries_from_docx(doc_file, sql_file)

        # Delete the downloaded .docx file
        os.remove(doc_file)

        print(f"Processed file: {file_name} -> {translated_name}.sql")


# Usage example
def main():
    # Load configuration from YAML file
    with open("config.yml", 'r') as config_file:
        config = yaml.safe_load(config_file)

    credentials_file = config['credentials_file']
    folder_id = config['folder_id']
    project_id = input("Enter the project ID: ")

    drive_service = authenticate_google_drive
