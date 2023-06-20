import MainMenu as Menu
from Util import db_helper as db
from Pages import LoginPage
from Pages.Useful import GeneralPage as General

class CopyrightPolicyPage:

    def menu(self):

        copyright_policy = """Copyright Policy:

We respect the intellectual property rights of others and expect our users to do the same. When using our platform, please ensure that you only upload and share content that you own or have the necessary permissions to use.

By posting content on our website, you grant us a non-exclusive, royalty-free, worldwide license to use, reproduce, modify, adapt, publish, translate, and distribute it. This license allows us to promote and improve our services while providing you with the best possible experience.

If you believe that your copyrighted work has been infringed upon, please notify us by providing the following information: (1) a description of the copyrighted work, (2) the location on our website where the infringing material is located, (3) your contact information, including name, address, telephone number, and email address, (4) a statement that you have a good faith belief that the use is not authorized by the copyright owner, and (5) a statement, made under penalty of perjury, that the information provided is accurate and that you are the copyright owner or authorized to act on behalf of the copyright owner.

We reserve the right to remove any infringing content and terminate the accounts of users who repeatedly infringe on intellectual property rights."""

        print()
        print(copyright_policy)
        print()

        choice = int(input("0.) Return to previous "))
        while True:
            if choice != 0:
                choice = int(input("\nInvalid input please select number next to navigation link: "))
            else:
                break
        if choice == 0:
            return
