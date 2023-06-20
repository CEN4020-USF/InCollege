import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class CookiePolicyPage:

    def menu(self):
        print()
        print("Our site uses essential cookies to function and provide an enjoyable experience.")
        print("Other non-essential cookies may be used to further customize and improve your experience.")
        print("By using our website, you agree to the use of essential cookies. ")
        print("Non-essential cookies can be disabled in the \"settings\" menu.")
        print()
        choice = int(input("0.) Return to previous "))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
