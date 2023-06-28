from Util import db_helper as db
from Pages import LoginPage as login


class ShowMyNetworkPage:
    def load_my_network(self):
        print("\n* My Network *\n")
        print("1.) Show My Connections")
        print("2.) Delete My Connections")
        print("3.) Delete My Pending Requests")
        print("0.) Return to Menu")
        choice = input("Enter Choice: ")

        if choice == "1":
            self.show_connections()
            self.load_my_network()
        elif choice == "2":
            self.delete_connections()
            self.load_my_network()
        elif choice == "3":
            self.delete_pending()
            self.load_my_network()
        elif choice == "0":
            return
        else:
            print(f"{choice} is an incorrect option. Please try again.")
            self.load_my_network()

    def show_connections(self):
        friends = db.get_friends(login.username)
        pending_friends = db.get_pending_to(login.username)
        self.print_friends(friends)
        self.print_pending(pending_friends)
        return

    @staticmethod
    def delete_connections():
        friends = db.get_friends(login.username)
        deleted_friend = input("Enter Username of Person to Unfriend: ")
        if deleted_friend not in friends:
            print(f"You are not friends with {deleted_friend}. Please try again")
            return
        deleted_friend = db.get_user(deleted_friend)
        db.delete_friend(login.username, deleted_friend)
        print(f"We have removed {deleted_friend} from your friends list!")
        return

    def delete_pending(self):
        friends = db.get_pending_to(login.username)
        delete_friend = input("Enter Username of Account to Delete Pending Request: ")
        if delete_friend not in friends:
            print(f"You did not have a pending friend request to {delete_friend}")
            return
        delete_friend = db.get_user(delete_friend)
        db.delete_pending(login.username, delete_friend)

    @staticmethod
    def print_friends(users):
        column_width = 25
        print("\n")
        if len(users) == 0:
            print("You currently have no connections")
            return
        print("Your Friends")
        menu = [["Username", "First Name", "Last Name", "University", "Major"],
                ["=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, ]]
        for user in users:
            user = db.get_user(user)
            profile = db.get_user_profile(user[0])
            user_attributes = [user[0], user[2], user[3], profile[2], profile[1]]
            menu.append(user_attributes)
        for row in menu:
            print("{:<25} | {:<25} | {:<25} | {:<25} | {:<25}".format(*row))
        print("\n")
        return

    @staticmethod
    def print_pending(users):
        column_width = 25
        print("\n")
        if len(users) == 0:
            print("You currently have no pending friend requests")
            return
        print("Your Pending Friend Requests")
        menu = [["Username", "First Name", "Last Name", "University", "Major"],
                ["=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, "=" * column_width, ]]
        for user in users:
            user = db.get_user(user)
            profile = db.get_user_profile(user[0])
            user_attributes = [user[0], user[2], user[3], profile[2], profile[1]]
            menu.append(user_attributes)
        for row in menu:
            print("{:<25} | {:<25} | {:<25} | {:<25} | {:<25}".format(*row))
        print("\n")
        return
