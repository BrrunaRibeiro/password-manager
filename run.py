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
SHEET = GSPREAD_CLIENT.open("password-manager-file").sheet1

class PasswordManager:
    """
    Defines main Class to run the program
    """
    def __init__(self, sheet):
        """
        
        """
        self.sheet = sheet

    def view_all_accounts(self):
        """
        
        """
        try:
            data = self.sheet.get_all_values()
            for account in data:
                print(account)
        except Exception as e:
            print(f"Error {e}") #double check if it works

    def add_account(self, account_name, username, password):
        """
        
        """
        try:
            data = [[account_name, username, password]]
            self.sheet.append_rows(data)
            print(f"{account_name}'s account added sucessfully.")
        except Exception as e:
            print(f"Error {e}") #double check if it works

    def view_specific_account(self, account_name):
        """
        Iterate's through the list of dictionaries returned by get_all_records().
        Finds the account name and prints the dictionary containg the account details.
        Prints an
        """
        try:
            data = self.sheet.get_all_records()
            account_name = account_name.strip()
            for account in data:
                if 'Account Name' in account and account["Account Name"].strip() == account_name:
                    print(account)
                    return
            print(f"{account_name}'s account not found.")
        except Exception as e:
            print(f"Error {e}") #double check if it works

    def update_account(self, account_name, new_username, new_password):
        """
        Iterate's through the list of dictionaries returned by get_all_records().
        The strip() method is used to help with typos and possible whitespaces issues.
        First the Account is deleted and then added again with the new_username and new_password.
        
        """
        try:
            data = self.sheet.get_all_records()
            #account_name = account_name.strip()
            for account in data:
                if account['Account Name'] == account_name:
                    self.sheet.delete_rows(data.index(account) + 2)

            data = [[account_name, new_username, new_password]]
            self.sheet.append_rows(data)
            print(f"{account_name}'s account updated successfully.")
            return
            print(f"{account_name}'s account not found.")
        except Exception as e:
            print(f"Error: {e}") #double check if it works
    
    def delete_account(self, account_name):
        """
        
        """
        try:
            data = self.sheet.get_all_records()
            #account_name = account_name.strip()
            for account in data:
                if account['Account Name'] == account_name:
                    self.sheet.delete_rows(data.index(account) + 2)
                    print(f"{account_name}'s account has been deleted.")
                    return
            print(f"{account_name}'s account not found.")
        except Exception as e:
            print(f"Error: {e}")
     
    def leave_application(self):
        """
        
        """
        print("Thank you for using Password Manager.")

def main():
    """
    Calls the main Class passing the SHEET variable as a argument.
    Prints the necessary information to the User on How to use the program.
    Validation for empty or incorrect input.
    """
    manager = PasswordManager(SHEET)
    print("Welcome to Password Manager")

    while True:
        print("\nPassword Manager Options: ")
        print("\n1. View all saved passwords")
        print("2. Add a new account")
        print("3. View an specific account' details")
        print("4. Update a saved password")
        print("5. Delete a account")
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
                account_name = input("Enter the Account Name to view(Ex:'Netflix'): ")
                manager.view_specific_account(account_name)
            elif choice == '4':
                account_name = input("Enter the Account Name to update: ")
                new_username = input("Enter your new username: ")
                new_password = input("Enter your new password: ")
                manager.update_account(account_name, new_username, new_password)
            elif choice == '5':
                account_name = input("Enter the Account Name you wish to delete: ")
                manager.delete_account(account_name)
            elif choice == '6':
                manager.leave_application()
                break
            else:
                raise ValueError(f"Valid Options are '1', '2', '3', '4', '5' and '6'. You provided '{choice}'")
        except ValueError as e:
            print(f"Invalid choice: {e}. Please enter a valid option.")
            return False
            #Must ask options again..
main()
