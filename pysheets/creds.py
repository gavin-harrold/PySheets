import os.path

from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import httplib2
from apiclient import discovery

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]


def generateCreds():
    secret_file = os.path.join(os.getcwd(), "pysheets/secret/gs_credentials.json")
    credentials = service_account.Credentials.from_service_account_file(
        secret_file, scopes=SCOPES
    )
    sheet_service = discovery.build("sheets", "v4", credentials=credentials)
    drive_service = discovery.build("drive", "v3", credentials=credentials)
    return sheet_service, drive_service
