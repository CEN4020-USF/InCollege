import pytest
import MainMenu
from Pages import LoginPage
from Pages import ConnectionsPage
from Util import db_helper as db


class TestConnections:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()
        self.connections = ConnectionsPage.ConnectionsPage()

    def test_search_for_student_last_name_existing(self, monkeypatch, capsys, mocker):
        inputs = ["1", "malloy", "0"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        user = ["benjamin", "landers"]
        with mocker.patch.object(db, 'check_name', return_value=user):
            self.connections.load_connections()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Users Found" in captured.out

    def test_search_student_last_name_does_not_exist(self, monkeypatch, capsys, mocker):
        inputs = ["1", "jim", "0"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Nothing is returned from db
        with mocker.patch.object(db, 'check_name', return_value=None):
            self.connections.load_connections()

        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "There were no users found with the last name," in captured.out

    def test_sent_request(self, monkeypatch, capsys, mocker):
        inputs = ["4", "test", "0"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        user = ["benjamin", "landers"]
        with mocker.patch.object(db, 'check_name', return_value=user):
            self.connections.load_connections()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "You sent a friend request to" in captured.out

    def test_sent_self_request(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "12", "4", "test", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        user = ["test", "Password1!"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=user):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "You can not friend yourself. Try Again." in captured.out

    def test_sent_request_already_friend(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "12", "4", "test", "4", "test", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["benjamin", "landers"]
        with mocker.patch.object(db, 'check_name', return_value=user):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Looks like you are either already friends or awaiting user to accept friend request." in captured.out


    def test_connections_returns_to_menu(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "12", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()

        # Capture the output
        captured = capsys.readouterr()
        # Validate the output
        assert "##################################################" in captured.out


    def test_pending_friend_request_decline(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "n", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user =["rmalloy1"]
        with mocker.patch.object(db, "get_pending_from", return_value=user):
            self.login.menu()

        captured = capsys.readouterr()

        # Validate the output
        assert "has been removed from your pending friend requests" in captured.out

    def test_pending_friend_request_accept(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "y", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user_from =["rmalloy1"]
        with mocker.patch.object(db, "get_pending_from", return_value=user_from):
            self.login.menu()
        

        captured = capsys.readouterr()

        # Validate the output
        assert "has been added" in captured.out

    def test_pending_friend_request_invalid_input(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "jank", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user_from =["rmalloy1"]
        with mocker.patch.object(db, "get_pending_from", return_value=user_from):
            self.login.menu()
        

        captured = capsys.readouterr()

        # Validate the output
        assert "Please select a valid option (Only enter a Y or N)" in captured.out

    def test_check_pending_requests(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "14", "1", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user_to =["rmalloy1"]
        with mocker.patch.object(db, "get_pending_to", return_value=user_to):
            self.login.menu()
    
        captured = capsys.readouterr()

        # Validate the output
        assert "Your Pending Friend Requests" in captured.out

    def test_searchBy_University_pass(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "12", "2", "test university", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["test", "Password1!"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=user):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Users Found" in captured.out

    def test_searchBy_University_fail(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "12", "2", "DummyStateUniversity", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["test", "Password1!"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=user):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "There were no users found at" in captured.out

    def test_searchBy_Major_Pass(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "12", "3", "new test major", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.connections.load_connections()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Users Found" in captured.out

    def test_searchBy_Major_fail(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "12", "3", "LoserDegree", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.connections.load_connections()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "There were no users found majoring in" in captured.out

    



    