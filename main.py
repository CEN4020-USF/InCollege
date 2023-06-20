# Imported Libraries

# Imported Files
import MainMenu as Menu
from Pages import LoginPage as Login

print("##################################################")
print("# Welcome to inCollege Command Line Environment  #")
print("#                                                #")
print("#        Developed By Team: New Mexico           #")
print("##################################################")

is_application_in_use = True
login_interface = Login.Login()
exit_screen = Menu.MainMenu()

while is_application_in_use:
    is_application_in_use = login_interface.menu()




