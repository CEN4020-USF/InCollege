# Import Section
from Util import db_helper as db
import MainMenu as menu
from Pages import LoginPage as login


class ConnectionsPage:
    def load_connections(self):
        print("\n* Search For Connections *\n")
        print("\nWould you like to find a connection with someone you know?")
        print("1.) Search by Last Name")
        print("2.) Search by University")
        print("3.) Search by Major")
        print("4.) Connect to User")
        print("0.) No return to previous")

        choice = input("\nPlease Enter Choice: ")
        if choice == "1":
            self.find_users_by_last_name()
            self.load_connections()
        elif choice == "2":
            self.find_users_by_university()
            self.load_connections()
        elif choice == "3":
            self.find_users_by_major()
            self.load_connections()
        elif choice == "4":
            self.connect()
            self.load_connections()
        elif choice == "0":
            return
        else:
            print("That is not a valid response. Please Try Again")
            self.load_connections()

    def find_users_by_last_name(self):
        last_name = input("Please enter last name: ")
        users = db.get_last_name(last_name.lower())
        if len(users) == 0:
            print(f"There were no users found with the last name, {last_name}")
            return
        self.print_users(users)
        return

    def find_users_by_major(self):
        return

    def find_users_by_university(self):
        return

    @staticmethod
    def connect():
        target_user = input("Enter Username: ")
        target_user = db.get_user(target_user)
        if target_user is None:
            print("User does not exist. Please search for users.")
            return
        print(f"You sent a friend request to {target_user[0]}. Waiting on their response.")
        db.add_pending(login.username, target_user)
        return

    def print_users(self, users):
        print("Users Found")
        print("Username | First Name | Last Name | University | Major")
        return