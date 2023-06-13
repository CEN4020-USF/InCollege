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

    def test_search_notifies_existing_user(self, monkeypatch, capsys, mocker):
        inputs = ["1", "Test", "Name", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        user = ["Test", "Name"]
        with mocker.patch.object(db, 'check_name', return_value=user):
            self.connections.load_connections()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "They are part of the InCollege system" in captured.out

    def test_search_notifies_user_does_not_exist(self, monkeypatch, capsys, mocker):
        inputs = ["1", "Test",  "Name", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Nothing is returned from db
        with mocker.patch.object(db, 'check_name', return_value=None):
            self.connections.load_connections()

        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "They are not yet a part of the InCollege system yet" in captured.out

    def test_connections_returns_to_menu(self, monkeypatch, capsys, mocker):
        inputs = ["2", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.connections.load_connections()

        # Capture the output
        captured = capsys.readouterr()
        # Validate the output
        assert "1.) Your Skill Development" in captured.out
