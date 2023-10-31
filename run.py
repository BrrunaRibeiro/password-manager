import gspread
from oauth2client.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets"
    "https://www.googleapis.com/auth/drive.file"
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.wtih_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("password_manager")