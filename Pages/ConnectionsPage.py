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
        print("0.) Return to previous")

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
        last_name = input("Please Enter Last Name: ")
        users = db.get_last_name(last_name.title())
        if len(users) == 0:
            print(f"There were no users found with the last name, {last_name}")
            return
        self.print_users(users)
        return

    def find_users_by_major(self):
        major = input("Please Enter Major: ")
        users = db.get_by_major(major.title())
        if len(users) == 0:
            print(f"There were no users found majoring in {major}")
            return
        self.print_users(users)
        return

    def find_users_by_university(self):
        university = input("Please Enter University: ")
        users = db.get_by_university(university.title())
        if len(users) == 0:
            print(f"There were no users found at {university}")
            return
        self.print_users(users)
        return

    @staticmethod
    def connect():
        target_user = input("Enter Username: ")
        target_user = db.get_user(target_user)
        if target_user is None:
            print("User does not exist. Please search for users.")
            return
        if target_user[0] == login.username:
            print("\nYou can not friend yourself. Try Again.")
            return
        if target_user[0] in db.get_friends(login.username) or target_user[0] in db.get_pending_to(login.username):
            print("Looks like you are either already friends or awaiting user to accept friend request. Please try again later")
            return
        print(f"You sent a friend request to {target_user[0]}. Waiting on their response.")
        db.add_pending(login.username, target_user)
        return

    @staticmethod
    def print_users(users):
        column_width = 25
        print("\n")
        print("Users Found")
        menu = [["Username", "First Name", "Last Name", "University", "Major"],
                ["=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, ]]
        for user in users:
            user = db.get_user(user)
            profile = db.get_user_profile(user[0])
            user_attributes = [user[0], user[2], user[3], profile[2], profile[1]]
            menu.append(user_attributes)
        for row in menu:
            print("{:<25} | {:<25} | {:<25} | {:<25} | {:<25}".format(*row))
        print("\n")
        return
