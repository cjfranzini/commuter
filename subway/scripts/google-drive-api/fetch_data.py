"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload
import io
import datetime

# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))

file_id = "1UBBEZq6WFXP2cvXAaVguNcw25dwKGPR1r6fueCW6WBQ"
request = drive_service.files().export_media(fileId=file_id,
                                             mimeType='text/csv')
date_string = datetime.datetime.today().strftime("%Y-%m-%d")
file_name = './data/commute_data-{}.csv'.format(date_string)
with open(file_name,'wb') as fh:
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))