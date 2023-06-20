from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class PressPage:

    def menu(self):
        print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports\n")
        choice = int(input("0.) Return to previous"))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            General.GeneralPage().menu()
