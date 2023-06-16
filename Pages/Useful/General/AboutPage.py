from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class AboutPage:

    def menu(self):
        print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide.\n")
        choice = int(input("0.) Return to previous"))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            General.GeneralPage().menu()
