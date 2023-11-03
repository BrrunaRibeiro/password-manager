"""
Imports the Gspred library.

To access all of it's functions, classes and methods.

Imports Credentials class.

Is part of the service_account function from the Google Auth library.
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("password-manager-file").sheet1


class PasswordManager:
    """Define main Class to run the program."""

    def __init__(self, sheet):
        """Innitialize the PasswordManager.

        It uses sheet(gspread.Worksheet) as a parameter,
        As it is the Google Sheet we will be using to store the account' data.
        """
        self.sheet = sheet

    def view_all_accounts(self):
        """View all account saved in the database.

        Iterates over the values returned from the get_all_records() method,
        Prints all saved accounts as a Dictionary,
        If there aren't any saved accounts, the Exception prints error message.
        """
        try:
            data = self.sheet.get_all_records()
            for account in data:
                print(account)
        except ImportError:  # perhaps another type of Error?
            print("\nError: No accounts found.")
            return False

    def add_account(self, account_name, username, password):
        """Add a new account to the database.

        Inputs are stored in the variable data.
        append_rows() adds the data to the worksheet in a new row.
        Print statement informs the user if it was sucessfully added.
        Exception prints the error message if the account cannot be added.
        """
        try:
            data = [[account_name, username, password]]
            self.sheet.append_rows(data)
            print(f"\n{account_name}'s account added sucessfully.")
            return True
        except ValueError:  # Perhaps use another type of Error?
            print("\nError: Unable to add account. Please try again.")
            return False

    def view_specific_account(self, account_name):
        """View a specific account based on the Account Name.

        Iterate's through the dictionaries returned by get_all_records().
        The strip() function removes leading and trailing spaces.
        Finds the match and prints the dictionary containg the account details.
        Except statement prints the raised error in case account not found.
        The print statement includes a suggetion to try to use capital letter.
        """
        try:
            data = self.sheet.get_all_records()
            account_name = account_name.strip()
            for account in data:
                if account.get('Account Name', '').strip() == account_name:
                    print(account)
                    return True
            raise ValueError(f"\n '{account_name}'s' account not found. ")
        except ValueError as e:
            print(f"\nError:{e}Did you mean {account_name} in capital letter?")
            return False

    def update_acc(self, account_name, new_username, new_password):
        """Update the database with the newest username and password.

        Iterate's through the dictionaries returned by get_all_records().
        The strip() function removes leading and trailing spaces.
        First, the Account is deleted, and then added with the new data.
        Print statement informs the user if it was sucessfully updated,
        Raises a ValueError if the account is not found,
        Exception statement prints error to the user.
        """
        try:
            data = self.sheet.get_all_records()
            account_name = account_name.strip()
            for account in data:
                if account['Account Name'] == account_name:
                    self.sheet.delete_rows(data.index(account) + 2)
                    data = [[account_name, new_username, new_password]]
                    self.sheet.append_rows(data)
                    print(f"\n{account_name}'s account updated successfully.")
                    return True
            raise ValueError(f"\n '{account_name}'s' account not found. ")
        except ValueError as e:
            print(f"\nError:{e} Try '{account_name}' in capital letter\n")
            return False

    def delete_account(self, account_name):
        """Delete the inpputted account.

        Iterates through the results from get_all_records(),
        Finds the matching for the account_name provided,
        If there's match, the delete_rows() will delete the account's data,
        Print() informs the user if the account was sucessfully deleted,
        If no matches, raises ValueError,
        Except statement prints the error and suggests to use capital letter.
        """
        try:
            data = self.sheet.get_all_records()
            account_name = account_name.strip()
            for account in data:
                if account['Account Name'] == account_name.strip():
                    self.sheet.delete_rows(data.index(account) + 2)
                    print(f"\n{account_name}'s account has been deleted.")
                    return True
            raise ValueError(f" {account_name}'s account not found. ")
        except ValueError as e:
            print(f"\nError:{e}Try'{account_name}' in capital letter")

    def leave_application(self):
        """Print a goodbye message and exits the application."""
        print("\nThank you for using Password Manager.\n")
        exit(self)


def main():
    """
    Call the main Class passing the SHEET variable as a argument.

    Prints information for the user to know how to use the program,
    While loop to keep presenting the options,
    Validation for empty or invalid inputs.
    """
    manager = PasswordManager(SHEET)
    while True:
        print("\nPassword Manager Options: ")
        print("\n1. View all saved passwords")
        print("2. Add a new account")
        print("3. View an specific account' details")
        print("4. Update a saved account")
        print("5. Delete an account")
        print("6. Leave the application")

        choice = input("\nEnter your choice(Ex:'2'): ")

        try:
            if choice == '1':
                manager.view_all_accounts()
            elif choice == '2':
                account_name = input("Enter the Account Name(Ex:'Netflix'): ")
                username = input("Enter the Username: ")
                password = input("Enter the Password: ")
                manager.add_account(account_name, username, password)
            elif choice == '3':
                account_name = input("Enter the Account Name(Ex:'Zoom'): ")
                manager.view_specific_account(account_name)
            elif choice == '4':
                account_name = input("Enter the Account Name to update: ")
                new_username = input("Enter your new username: ")
                new_password = input("Enter your new password: ")
                manager.update_acc(account_name, new_username, new_password)
            elif choice == '5':
                account_name = input("Enter the Account Name to delete: ")
                manager.delete_account(account_name)
            elif choice == '6':
                manager.leave_application()
                break
            else:
                raise ValueError(f"Valid:'1,2,3,4,5,6'. Entered '{choice}'")
        except ValueError as e:
            print(f"Invalid choice: {e}. Please enter a valid option.")


print("Welcome to Password Manager")
main()
