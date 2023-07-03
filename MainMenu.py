from Pages import SkillsPage as Skills
from Pages import LoginPage as login
from Pages import ConnectionsPage as Connect
from Pages import JobOpportunitiesPage as Job
from Pages import ShowMyNetwork as Network, UserProfilePage as Profile
from Pages.Useful import BrowseInCollegePage as Browse, DirectoriesPage as Directory, GeneralPage as General, BusinessSolutionsPage as Business
from Pages.InCollegeImportant import AccessibilityPage as Accessibility,\
    BrandPolicyPage as Brand, CopyrightPage as Copyright, \
    UserAgreementPage as UserAgreement, CookiePolicyPage as Cookie, \
    CopyrightPolicyPage as CopyPolicy, About as About, \
    LanguagePage as Lang, PrivacyPage as Privacy
from Util import db_helper as db


class MainMenu:
    def __init__(self):
        self.job_page = Job.JobOpportunitiesPage()
        self.connect_page = Connect.ConnectionsPage()
        self.skills_page = Skills.SkillsPage()
        self.network = Network.ShowMyNetworkPage()
        self.profile = Profile.UserProfilePage()

    def invalid_response(self, invalid_selection):
        print(f"{invalid_selection} is not a valid option. Please only enter the number")
        print("next to the option you would like to navigate to.")

    def selected_menu_option(self, user_choice):
        if user_choice == 11:
            self.skills_page.select_skill()
            return True
        elif user_choice == 12:
            self.connect_page.load_connections()
            return True
        elif user_choice == 13:
            self.job_page.load_job_opportunities()
            return True
        elif user_choice == 14:
            self.network.load_my_network()
            return True
        elif user_choice == 15:
            self.profile.load_profile(login.username)
            return True
        elif user_choice == 16:
            return False
        elif user_choice == 21:
            General.GeneralPage().menu()
            return True
        elif user_choice == 22:
            Browse.BrowseInCollegePage().menu()
            return True
        elif user_choice == 23:
            Business.BusinessSolutionsPage().menu()
            return True
        elif user_choice == 24:
            Directory.DirectoriesPage().menu()
            return True
        elif user_choice == 31:
            Copyright.CopyrightPage().menu()
            return True
        elif user_choice == 32:
            About.AboutPage().menu()
            return True
        elif user_choice == 33:
            Accessibility.AccessibilityPage().menu()
            return True
        elif user_choice == 34:
            UserAgreement.UserAgreementPage().menu()
            return True
        elif user_choice == 35:
            Cookie.CookiePolicyPage().menu()
            return True
        elif user_choice == 36:
            CopyPolicy.CopyrightPolicyPage().menu()
            return True
        elif user_choice == 37:
            Brand.BrandPolicyPage().menu()
            return True
        elif user_choice == 38:
            Privacy.PrivacyPolicyPage().menu()
            return True
        elif user_choice == 39:
            Lang.LanguagePage().menu()
            return True
        else:
            self.invalid_response(user_choice)
            return True

    def main_menu_options(self):
        if db.get_pending_from(login.username) is not None:
            self.pending_friends_prompt()
        while True:
            self.print_menu()
            choice = int(input("\nPlease enter where you would like to navigate: "))
            is_exit = self.selected_menu_option(choice)
            if (choice == 16):
                return self.exit()
        
    @staticmethod
    def exit():
        print()
        print("##################################################")
        print("#                                                #")
        print("#        Thank you for using inCollege           #")
        print("#                                                #")
        print("##################################################")
        return 0


    def print_menu(self):
        column_width = 31
        print("\n")
        menu = [["Main Menu Options", "Useful Links", "Important InCollege Links"],
                ["="*column_width, "="*column_width, "="*column_width],
                ["11.) Your Skill Development", "21.) General", "31.) Copyright Notice"],
                ["12.) Your Connections", "22.) Browse InCollege", "32.) About"],
                ["13.) Job/Internship Prospects", "23.) Business Solutions", "33.) Accessibility"],
                ["14.) Show My Network", "24.) Directories", "34.) User Agreement"],
                ["15.) Show Profiles", "", "35.) Cookie Policy"],
                ["16.) Exit", "", "36.) Copyright Policy"],
                ["", "", "37.) Brand Policy"],
                ["", "", "38.) Privacy Policy"],
                ["", "", "39.) Language Settings"], ]
        for row in menu:
            print("{:<31} | {:<31} | {:<31} ".format(*row))
        print("\n")

    def pending_friends_prompt(self):
        pending_friends = db.get_pending_from(login.username)
        current_user = db.get_user(login.username)
        for friend in pending_friends:
            friend = db.get_user(friend)
            choice = input(f"\n{friend[0]} has sent you a friend request. Would you like to accept? (Y/N)").lower()
            if choice == "y":
                print(f"{friend[0]} has been added")
                db.add_friend(login.username, friend)
                db.delete_pending(friend[0], current_user)
            elif choice == "n":
                print(f"{friend[0]} has been removed from your pending friend requests")
                db.delete_pending(friend[0], current_user)
            else:
                print("Please select a valid option (Only enter a Y or N)")
        return
