#Imports the Gspred library to access all of it's  functions, class or methods within it.
import gspread

#Imports Credentials class(part of the service_account function from the Google Auth library).
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("password-manager-file")

class PasswordManager:
    """
    Defines main Class to run the program
    """
    def __init__(self, sheet):
        self.sheet = sheet


def main():
    """
    Calls the main Class with the SHEET variable as a argument.
    """
    manager = PasswordManager(SHEET)

main()