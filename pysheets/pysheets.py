"""
file: pysheets.py
author: Gavin Harrold
desc: CLI for creating Google spreadsheets using Python and Google Sheets API
"""

import typer
from typing import List
from pysheets import __app_name__, __version__
from pysheets.creds import *

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

cli = typer.Typer()
sheet_service, drive_service = generateCreds()


@cli.command()
def help():
    print("HELP")


@cli.command()
def new_folder(name: str):
    print(f"Creating new folder with name {name}...")
    file_metadata = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder",
    }

    file = drive_service.files().create(body=file_metadata, fields="id").execute()
    folder_id = file.get("id")

    new_permissions = {
        "type": "group",
        "role": "writer",
        "emailAddress": "gavinsharrold@gmail.com",
    }

    permission_response = (
        drive_service.permissions()
        .create(fileId=folder_id, body=new_permissions)
        .execute()
    )
    print(f"Done!")


@cli.command()
def new(name: str):
    print(f"Creating new Sheet with name {name}...")

    gc = generateCreds()
    try:
        service = build("sheets", "v4", credentials=creds)
        spreadsheet = {"properties": {"title": name}}
        spreadsheet = (
            service.spreadsheets()
            .create(body=spreadsheet, fields="spreadsheetId")
            .execute()
        )
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get("spreadsheetId")
    except HttpError as err:
        print(f"An error occurred: {err}")
        return err
