# Imports
from Util import db_helper as db
import MainMenu as menu
from Pages.skills import TeamworkPage as teamwork
from Pages.skills import OrganizationPage as organization
from Pages.skills import CommunicationPage as communication
from Pages.skills import ProblemSolvingPage as solving
from Pages.skills import ProjectManagementPage as management


class SkillsPage:
    @staticmethod
    def select_skill():
        print("Please Select a Skill")
        print("1.) Communication")
        print("2.) Project Management")
        print("3.) Teamwork")
        print("4.) Organization")
        print("5.) Problem Solving")
        print("9.) Main Menu")
        choice = input("Please enter a skill you would like to work on: ")

        if choice == "1":
            communication.CommunicationPage.load_communication()
        elif choice == "2":
            management.ProjectManagementPage.load_project_management()
        elif choice == "3":
            teamwork.TeamworkPage.load_teamwork()
        elif choice == "4":
            organization.OrganizationPage.load_organization()
        elif choice == "5":
            solving.ProblemSolvingPage.load_problem_solving()
        elif choice == "9":
            return menu.MainMenu.main_menu_options
        else:
            print("Please try again \n")
            SkillsPage.select_skill()



