from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import secretsvar
import os

class GspreadOeration:

    SERVICE_ACCOUNT_FILE = secretsvar.SERVICE_ACCOUNT_FILE
    SCOPES = secretsvar.SCOPES
    SPREADSHEET_ID = secretsvar.SPREADSHEET_ID
    
    def __init__(self) -> None:
        try:
            creds = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
            service = build("sheets", "v4", credentials=creds)
            sheet = service.spreadsheets()
            self.sheet=sheet
        except HttpError as e:
            self.sheet=None

    def append_data(self,values):
        body = {"values": [values]}
        try:
            result = (
                self.sheet.values().append(
                    spreadsheetId=self.SPREADSHEET_ID,
                    range="Sheet1",
                    body=body,
                    valueInputOption="RAW",
                ).execute()
            )
            return result
        except HttpError as err:
            return err

    def show_data(self):
        try:
            result = self.sheet.values().get(spreadsheetId=self.SPREADSHEET_ID, range="Sheet1").execute()
            val = result.get("values", [])
            return val
        except HttpError as err:
            return err

