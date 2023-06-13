from Pages import SkillsPage as Skills
from Pages import ConnectionsPage as Connect
from Pages import JobOpportunitiesPage as Job


class MainMenu:
    def __init__(self):
        self.job_page = Job.JobOpportunitiesPage()
        self.connect_page = Connect.ConnectionsPage()
        self.skills_page = Skills.SkillsPage()

    def invalid_response(self, invalid_selection):
        print(f"{invalid_selection} is not a valid option. Please only enter the number")
        print("next to the option you would like to navigate to.")

    def selected_menu_option(self, user_choice):
        if user_choice == 1:
            self.skills_page.select_skill()
            return True
        elif user_choice == 2:
            self.connect_page.load_connections()
            return True
        elif user_choice == 3:
            self.job_page.load_job_opportunities()
            return True
        elif user_choice == 4:
            return False
        else:
            self.invalid_response(user_choice)
            return True

    def main_menu_options(self):
        while True:
            print("1.) Your Skill Development")
            print("2.) Your Connections")
            print("3.) Job/Internship Opportunities")
            print("\n4.) Exit")
            choice = int(input("\nPlease enter where you would like to navigate: "))
            is_exit = self.selected_menu_option(choice)
            if (choice == 4):
                 return is_exit

    @staticmethod
    def exit():
        print()
        print("##################################################")
        print("#                                                #")
        print("#        Thank you for using inCollege           #")
        print("#                                                #")
        print("##################################################")
        return 0
