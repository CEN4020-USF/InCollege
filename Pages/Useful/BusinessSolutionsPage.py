from Util import db_helper as db
import MainMenu as Menu
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class BusinessSolutionsPage:

    def menu(self):
        print("\nunder construction\n")
        choice = int(input("0.) Return to previous"))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
