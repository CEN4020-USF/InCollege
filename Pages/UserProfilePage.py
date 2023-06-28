# Import Section
from Util import db_helper as db
from Pages import LoginPage as login


class UserProfilePage:
    def load_profile(self, user):
        current_user = db.get_user(user)
        user_profile = db.get_user_profile(user)
        print(f"\n* {current_user[2]} {current_user[3]}'s User Profile*\n\n")
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
        if current_user[0] == login.username:
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
        print("\nWhat would you like to edit?")
        print("1.) Title")
        print("2.) Major")
        print("3.) University")
        print("4.) About")
        print("0.) Save Changes and Return")
        choice = input("Enter Choice: ")

        if choice == "1":
            title = input("Enter Title: ")
            db.set_user_profile(user, "Title", title)
            self.edit(user)
        elif choice == "2":
            major = input("Enter Major: ").title()
            db.set_user_profile(user, "Major", major)
            self.edit(user)
        elif choice == "3":
            uni = input("Enter University: ").title()
            db.set_user_profile(user, "University", uni)
            self.edit(user)
        elif choice == "4":
            about = input("Tell us About Yourself: ")
            db.set_user_profile(user, "About", about)
            self.edit(user)
        elif choice == "0":
            user_check = db.get_user_profile(user)
            if None not in user_check:
                db.set_user_profile(user, "IsCreated", 1)
            return
        else:
            print(f"{choice} is not a valid choice.")
            self.edit(user)

    def view_friends(self, user):
        return

    def print_jobs(self, user):
        return

    def print_education(self, user):
        return
