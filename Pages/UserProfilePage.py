# Import Section
from Util import db_helper as db
from Pages import LoginPage as login
from Pages import JobOpportunitiesPage as jobs


class UserProfilePage:
    def load_profile(self, user):
        current_user = db.get_user(user)
        user_profile = db.get_user_profile(user)
        print(f"\n* {current_user[2]} {current_user[3]}'s User Profile *\n\n")
        print(f"Title: {user_profile[0]}")
        print(f"Major: {user_profile[1]}")
        print(f"University: {user_profile[2]}\n")
        print("About: ")
        print(f"{user_profile[3]}\n")
        self.print_jobs(user)
        self.print_education(user)
        self.print_menu(user)
        return

    def print_menu(self, user):
        current_user = db.get_user(user)
        if current_user[0] != login.username:
            input("Press Enter to Return to Your Profile")
            return
        print("\nMenu: ")
        print("1.) Edit Profile")
        print("2.) View Friend's Profile")
        print("0.) Return to Menu")
        choice = input("Enter Choice: ")
        if choice == "1":
            self.edit(current_user[0])
            self.load_profile(current_user[0])
        elif choice == "2":
            self.view_friends(user)
            self.load_profile(current_user[0])
        elif choice == "0":
            return
        else:
            print(f"{choice} is not a valid response")
            self.load_profile(current_user[0])

    def edit(self, user):
        print("\nWhat would you like to edit?")
        print("1.) Title")
        print("2.) Major")
        print("3.) University")
        print("4.) About")
        print("5.) Add Professional Experience")
        print("6.) Add Education")
        print("0.) Save Changes and Return")
        choice = input("Enter Choice: ")

        match choice:
            case "1":
                title = input("Enter Title: ")
                db.set_user_profile(user, "Title", title)
                self.edit(user)
            case "2":
                major = input("Enter Major: ").title()
                db.set_user_profile(user, "Major", major)
                self.edit(user)
            case "3":
                uni = input("Enter University: ").title()
                db.set_user_profile(user, "University", uni)
                self.edit(user)
            case "4":
                about = input("Tell us About Yourself: ")
                db.set_user_profile(user, "About", about)
                self.edit(user)
            case "5":
                title = input("What is the title of the job? ")
                description = input("Give a description of the job ")
                employer = input("Who is the employer of the job? ")
                location = input("Where is the location of the job? ")
                start = input("When did you start working here? ")
                end = input("When did you stop working here? ")
                db.add_job(login.username, title, description, employer, location, None, start, end)
                self.edit(user)
            case "6":
                school = input("Name of School: ").title()
                degree = input("Name of Degree: ").title()
                start = input("Start Year: ")
                end = input("End Year: ")
                db.add_education(user, school, degree, start, end)
                self.edit(user)
            case "0":
                user_check = db.get_user_profile(user)
                if None not in user_check:
                    db.set_user_profile(user, "IsCreated", 1)
                return
            case _:
                print(f"{choice} is not a valid choice.")
                self.edit(user)
    
    def view_friends(self, user):
        column_width = 25
        friends = db.get_friends(user)

        if len(friends) == 0:
            print("\nThere are no friends on your friends list")
            return

        print("\n")
        print("Your Friends")
        menu = [["Username", "First Name", "Last Name", "University", "Major", "Profile Created"],
                ["=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width]]
        for friend in friends:
            friend = db.get_user(friend)
            friend_profile = db.get_user_profile(friend[0])
            if friend_profile[4]:
                is_created = "View Profile"
            else:
                is_created = ""
            user_attributes = [friend[0], friend[2], friend[3], friend_profile[2], friend_profile[1], is_created]
            menu.append(user_attributes)
        for row in menu:
            print("{:<25} | {:<25} | {:<25} | {:<25} | {:<25} | {:<25}".format(*row))
        print("\n")

        print("Would you like to view a friend's profile")
        print("1.) Select Account")
        print("0.) Return to Profile")
        choice = input("Enter Choice: ")
        if choice == "1":
            friend_username = input("Enter Friend's Username: ")
            if (friend_username not in friends) or (db.get_user_profile(friend_username)[4] == 0):
                print("\nLooks like the user you are trying to connect to either: 1.) Is not a friend or 2.) Does not have a profile set up")
                return
            self.load_profile(friend_username)
            self.view_friends(user)
        elif choice == "0":
            return
        else:
            print(f"{choice} is not a valid choice.")
            self.view_friends(user)
        return

    @staticmethod
    def print_jobs(user):
        column_width = 35
        jobs = db.get_job_by_user(user)
        if jobs is None or len(jobs) == 0:
            print("There is no relevant professional experience yet.")
            return

        print("\nProfessional Experience: ")
        menu = [["Title", "Employer", "Date Started", "Date Ended", "Location", "Description"],
                ["=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width]]
        for job in jobs:
            job_attributes = [job[0], job[2], job[6], job[7], job[3], job[1]]
            menu.append(job_attributes)
        for row in menu:
            print("{:<35} | {:<35} | {:<35} | {:<35} | {:<35} | {:<35}".format(*row))
        print("\n")

    @staticmethod
    def print_education(user):
        column_width = 35
        education = db.get_education(user)
        if education is None or len(education) == 0:
            print("There is no relevant education experience yet")
            return

        print("\nEducation: ")
        menu = [["School", "Degree", "Start Year", "End Year"],
                ["=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width]]
        for school in education:
            education_attributes = [school[0], school[1], school[2], school[3]]
            menu.append(education_attributes)
        for row in menu:
            print("{:<35} | {:<35} | {:<35} | {:<35}".format(*row))
        print("\n")

