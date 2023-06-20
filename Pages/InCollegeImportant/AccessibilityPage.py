import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class AccessibilityPage:

    def menu(self):
        print()
        print("#"*70)
        print("# Accessibility Statement                                            #")
        print("#                                                                    #")
        print("# Our website has been developed with the intention of being         #")
        print("# used by all possible users, regardless of any disability or age.   #")
        print("#"*70)
        print()

        choice = int(input("0.) Return to previous "))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
