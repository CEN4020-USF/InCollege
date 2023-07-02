from Util import db_helper as db
from Util import db_helper as db
from Pages import LoginPage as login


class LanguagePage:

    def menu(self):
        #if login.username == "":
        if not db.is_user_signed_in():
            print("\nPlease login before trying to edit language settings\n")
            return

        print("\n* Language *\n")
        print(f"Current Language: {db.get_user(login.username)[7]}\n")
        print("Set Language:")
        print("1.) English")
        print("2.) Spanish")
        print("0.) Return")
        choice = input("Enter Choice: ")

        if choice == "1":
            db.change_language(db.get_user(login.username)[0], "English")
            print("Your language has been set to English!")
        elif choice == "2":
            db.change_language(db.get_user(login.username)[0], "Spanish")
            print("Your language has been set to Spanish!")
        elif choice == "0":
            return
        else:
            print(f"{choice} is not valid. Please try again.")
            self.menu()
