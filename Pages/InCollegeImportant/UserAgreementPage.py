import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class UserAgreementPage:

    def menu(self):

        user_agreement = """User Agreement:

Welcome to InCollege! By accessing and using our website, you agree to comply with the following terms and conditions:

Eligibility: You must be a college student or alumni to use InCollege. You are responsible for providing accurate and up-to-date information during registration.

User Conduct: You agree to use InCollege responsibly and respect the rights of others. You will not post inappropriate, unlawful, or misleading content, engage in harassment or spamming, or violate any applicable laws.

Privacy: We value your privacy and will handle your personal information in accordance with our Privacy Policy.

Intellectual Property: All content on InCollege, including trademarks, logos, and user-generated content, is protected by intellectual property laws. You may not use or distribute such content without permission.

Termination: We reserve the right to suspend or terminate your account if you violate these terms or engage in harmful or fraudulent activities.

By using InCollege, you acknowledge and agree to abide by these terms. Happy networking!"""

        print()
        print(user_agreement)
        print()

        choice = int(input("0.) Return to previous "))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
