import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class AboutPage:

    def menu(self):

        print()
        print("InCollege is designed to be an alternative to LinkedIn for college ")
        print("students who might lack the experience or resume needed to effectively")
        print("utilize the platform. ")
        print()
        print("Our Mission")
        print()
        print("To help college students gain access to a networking platform that helps them")
        print("take their first steps into the process of searching for and applying to internships.")
        print()
        print("Our Vision")
        print()
        print("For college students to use our tools to connect with other students and gain insight")
        print("into how the workforce of their particular field operates.")
        print()


        choice = int(input("0.) Return to previous "))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
