from Pages.Useful import GeneralPage as General


class CareersPage:

    def menu(self):
        print("under construction")
        choice = input("0.) Return to previous")
        while True:
            if choice != "0":
                choice = input("\nInvalid input please select number next to navigation link: ")
            else:
                break
        if choice == "0":
            General.GeneralPage().menu()
