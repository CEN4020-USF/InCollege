from Util import db_helper as db
from Pages import LoginPage as login


class PrivacyPolicyPage:

    def menu(self):
        print("\n* Privacy Policy Page *\n")
        print("1.) Guest Policy Controls")
        print("0.) Return")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            self.guest_controls_menu()
            self.menu()
        elif choice == 0:
            return
        else:
            print(f"{choice} is not a supported option. Please try again")
            self.menu()
    def guest_controls_menu(self):
        #if login.username == "":
        if db.is_user_signed_in() == False:
            print("Please sign in to edit settings")
            return

        email = db.get_user(login.username)[4]
        sms = db.get_user(login.username)[5]
        advertising = db.get_user(login.username)[6]

        print("\n* Guest Controls Page *\n")
        print(f"1.) Press to Toggle Email Notifications\t\t Current: {email}")
        print(f"2.) Press to Toggle SMS Notifications\t\t Current: {sms}")
        print(f"3.) Press to Toggle Targeted Advertising\t Current: {advertising}")
        print("4.) Return")
        print("1 = ON\t0 = OFF")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            email = self.toggler(email)
            db.toggle_email(login.username, email)
            print("Email Notifications Updated")
            self.guest_controls_menu()
        elif choice == 2:
            sms = self.toggler(sms)
            db.toggle_sms(login.username, sms)
            print("SMS Notifications Updated")
            self.guest_controls_menu()
        elif choice == 3:
            advertising = self.toggler(advertising)
            db.toggle_advertising(login.username, advertising)
            print("Targeted Advertising Updated")
            self.guest_controls_menu()
        elif choice == 4:
            return
        else:
            print(f"{choice} is not a supported option. Please try again")
            self.guest_controls_menu()

    def toggler(self, toggle):
        if toggle == 1:
            return 0
        else:
            return 1
