from Util import db_helper as db
from Util import db_helper as db
from Pages import LoginPage as login


class LanguagePage:

    def menu(self):
        #if login.username == "":
        if db.is_user_signed_in() == False:
            print("\nPlease login before trying to edit language settings\n")
            return

        print("\n* Language *\n")
        print("Set Language:")
        print("1.) English")
        print("2.) Spanish")
        print("0.) Return")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            db.change_language(db.get_user(login.username)[0], "English")
            print("Your language has been set to English!")
        elif choice == 2:
            db.change_language(db.get_user(login.username)[0], "Spanish")
            print("Your language has been set to Spanish!")
        elif choice == 0:
            return
