import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class CopyrightPage:

    def menu(self):
        print()
        print("Copyright 2023 InCollege (Team New Mexico)")
        print()
        choice = int(input("0.) Return to previous "))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
