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
        inputs = ["1", "landers", "0"]
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

    def test_sent_request_already_friend(self, monkeypatch, capsys, mocker):
        inputs = ["4", "rm", "0", 15]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["blanders1", "Forgaming1!"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.connections.load_connections()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Looks like you are either already friends or awaiting user to accept friend request" in captured.out


    def test_connections_returns_to_menu(self, monkeypatch, capsys, mocker):
        inputs = ["0"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.connections.load_connections()

        # Capture the output
        captured = capsys.readouterr()
        # Validate the output
        assert "1.) Your Skill Development" in captured.out
