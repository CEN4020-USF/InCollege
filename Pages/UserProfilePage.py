# Import Section
from Util import db_helper as db
from Pages import LoginPage as login
from Pages import JobOpportunitiesPage as jobs


class UserProfilePage:
    def load_profile(self, user):
        current_user = db.get_user(user)
        user_profile = db.get_user_profile(user)
        print(f"\n* {current_user[2]} {current_user[3]}'s User Profile *\n\n")
        print(f"Title: {user_profile[0]}")
        print(f"Major: {user_profile[1]}")
        print(f"University: {user_profile[2]}\n")
        print("About: ")
        print(f"{user_profile[3]}\n")
        self.print_jobs(user)
        self.print_education(user)
        self.print_menu(user)
        return

    def print_menu(self, user):
        current_user = db.get_user(user)
        if current_user[0] != login.username:
            input("Press Enter to Return to Your Profile")
            return
        print("\nMenu: ")
        print("1.) Edit Account")
        print("2.) View Friends")
        print("0.) Return to Menu")
        choice = input("Enter Choice: ")
        if choice == "1":
            self.edit(current_user[0])
            self.load_profile(current_user[0])
        elif choice == "2":
            self.view_friends(user)
            self.load_profile(current_user[0])
        elif choice == "0":
            return
        else:
            print(f"{choice} is not a valid response")
            self.load_profile(current_user[0])

    def edit(self, user):
        return

    def view_friends(self, user):
        column_width = 25
        friends = db.get_friends(user)

        if len(friends) == 0:
            print("\nCurrently, you have no friends")
            return

        print("\n")
        print("Your Friends")
        menu = [["Username", "First Name", "Last Name", "University", "Major", "Profile Created"],
                ["=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width]]
        for friend in friends:
            friend = db.get_user(friend)
            friend_profile = db.get_user_profile(friend[0])
            if friend_profile[4]:
                is_created = "View Profile"
            else:
                is_created = ""
            user_attributes = [friend[0], friend[2], friend[3], friend_profile[2], friend_profile[1], is_created]
            menu.append(user_attributes)
        for row in menu:
            print("{:<25} | {:<25} | {:<25} | {:<25} | {:<25} | {:<25}".format(*row))
        print("\n")

        print("Would you like to view a friend's profile")
        print("1.) Select Account")
        print("0.) Return to Profile")
        choice = input("Enter Choice: ")
        if choice == "1":
            friend_username = input("Enter Friend's Username: ")
            if (friend_username not in friends) or (db.get_user_profile(friend_username)[4] == 0):
                print("\nLooks like the user you are trying to connect to either: 1.) Is not a friend or 2.) Does not have a profile set up")
                return
            self.load_profile(friend_username)
            self.view_friends(user)
        elif choice == "0":
            return
        else:
            print(f"{choice} is not a valid choice.")
            self.view_friends(user)
        return

    @staticmethod
    def print_jobs(user):
        return

    @staticmethod
    def print_education(user):
        return

