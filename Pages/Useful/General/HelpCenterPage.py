from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class HelpCenterPage:

    def menu(self):
        print("\nWe're here to help!\n")
        choice = int(input("0.) Return to previous"))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            General.GeneralPage().menu()
