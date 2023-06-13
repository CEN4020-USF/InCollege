# Imports
from Util import db_helper as db
import MainMenu as menu
from Pages import LoginPage as login

class JobOpportunitiesPage:
    def load_job_opportunities(self):
        print("1.) Post a job")
        print("9.) Main menu")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            self.post_job()
        elif choice == 9:
            return menu.MainMenu().main_menu_options()
        else:
            print("Please try again \n")
    def post_job(self):
        if (db.count_jobs() >= 5):
            print("Number of jobs permitted exceeded, going back to main menu\n")
            return menu.MainMenu.main_menu_options
        title = input("What is the title of the job? ")
        description = input("Give a description of the job ")
        employer = input("Who is the employer of the job? ")
        location = input("Where is the location of the job? ")
        salary = input("What is the yearly salary of the job? ")
        created_by = db.get_user(login.username)[0]    
        db.add_job(title, description, employer, location, salary, created_by)
        print("Job Added")
        self.load_job_opportunities()