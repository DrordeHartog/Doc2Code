# Doc2Code
This Python script extracts SQL queries from .docx files, creates corresponding .sql files, and supports Google Drive integration for processing files in a specified folder.

## Prerequisites

- Python 3.x
- Required Libraries:
  - python-docx
  - google-api-python-client
  - google-auth-httplib2
  - google-auth-oauthlib
  - googletrans

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
##Configuration
### Google Drive Integration
To use the Google Drive integration feature, you need to set up the Google Drive API and obtain credentials. Follow these steps:

Create a new project in the Google Cloud Platform (GCP) Console.

Enable the Google Drive API for your project.

Create a service account key for your project and download the JSON key file.

Share the target Google Drive folder with the email address associated with the service account.

Create a configuration file named config.yml in the script directory and specify the following:
```
credentials_file: <path_to_credentials_file.json>
folder_id: <google_drive_folder_id>
```
Replace <path_to_credentials_file.json> with the path to the downloaded JSON key file, and <google_drive_folder_id> with the ID of the target Google Drive folder.

###Language Support
Currently, the scripts supports only Hebrew translation. Any file name in hebrew will be translated to english.
##Usage
Place the .docx files containing SQL queries in the specified Google Drive folder.

Open a terminal or command prompt.

Run the script using the following command:

```bash
Copy code
python script.py
```
Follow the prompts and provide the necessary information when prompted, such as the project ID.

The script will process the .docx files, extract SQL queries, translate file names (if needed), and save the SQL queries as .sql files.


###License
This script is released under the MIT License.

#Acknowledgements
This script utilizes the following libraries:
```
python-docx
google-api-python-client
googletrans
```
Contact
For any questions or support requests, please contact Your DrordeHartog on github


Feel free to customize the content of the readme file according to your specific needs, adding or removing sections as necessary.



