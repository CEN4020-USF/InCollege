import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class BrowseInCollegePage:

    def menu(self):
        print("\nunder construction\n")
        choice = input("0.) Return to previous")
        while True:
            if choice != "0":
                choice = input("\nInvalid input please select number next to navigation link: ")
            else:
                break
        if choice == "0":
            return
