
from Pages.Useful import GeneralPage as General

class DeveloperPage:

    def menu(self):
        print("under construction")
        choice = int(input("0.) Return to previous"))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            General.GeneralPage().menu()
