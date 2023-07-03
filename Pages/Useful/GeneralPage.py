from Pages.Useful.General import AboutPage as About, HelpCenterPage as Help, PressPage as Press, BlogPage as Blog, \
    CareersPage as Career, DevelopmentPage as Developer
from Pages import LoginPage
from Util import db_helper as db

from Util import db_helper as db
import MainMenu as Menu

class GeneralPage:

    def menu(self):
        print("\n** General Links **\n")
        print("1.) Sign Up")
        print("2.) Help Center")
        print("3.) About")
        print("4.) Press")
        print("5.) Blog")
        print("6.) Careers")
        print("7.) Developers")
        print("0.) Return To Menu")

        choice = input("Enter Option: ")

        if choice == "1":
            if db.is_user_signed_in():
                print("\n**It seems you are already signed in.**")
                return self.menu()
            print("\n1.) Sign In")
            print("2.) Create Account")
            print("0.) Return to previous page")
            option = input("Enter option: ")
            while True:
                if option != "1" and option != "2" and option != "0":
                    option = input("Invalid input please enter 1, 2, or 0: ")
                else:
                    break
            if option == "1":
                LoginPage.Login().sign_in()
            elif option == "2":
                LoginPage.Login().create_account()
            elif option == "0":
                GeneralPage().menu()

        elif choice == "2":
            Help.HelpCenterPage().menu()
        elif choice == "3":
            About.AboutPage().menu()
        elif choice == "4":
            Press.PressPage().menu()
        elif choice == "5":
            Blog.BlogPage().menu()
        elif choice == "6":
            Career.CareersPage().menu()
        elif choice == "7":
            Developer.DeveloperPage().menu()
        elif choice == "0":
            if not db.is_user_signed_in():
                LoginPage.Login().menu()
            else:
                return
        else:
            print(f"{choice} is not supported. Please try again")
            self.menu()
