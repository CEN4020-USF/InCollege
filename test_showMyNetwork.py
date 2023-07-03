import pytest
import MainMenu
from Pages import LoginPage
from Pages import ConnectionsPage
from Util import db_helper as db


class TestShowNetwork:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()
        self.connections = ConnectionsPage.ConnectionsPage()

    def test_show_friends(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "14", "1", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()

        captured = capsys.readouterr()

        # Validate the output
        assert "Your Friends" in captured.out

    def test_NoFriends_show_friends(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "14", "1", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'get_friends', return_value=''):
            self.login.menu()

        captured = capsys.readouterr()

        # Validate the output
        assert "You currently have no connections" in captured.out

    def test_delete_friends(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "14", "2","rmalloy1", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["rmalloy1"]
        with mocker.patch.object(db, 'get_friends', return_value=user):
            self.login.menu()

        captured = capsys.readouterr()

        # Validate the output
        assert "We have removed" in captured.out

    def test_delete_friends_wrong_input(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "14", "2","janky", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["jimmy"]
        with mocker.patch.object(db, 'get_friends', return_value=user):
            self.login.menu()

        captured = capsys.readouterr()

        # Validate the output
        assert "You are not friends with" in captured.out

    def test_Network_returns_to_menu(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "14", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()

        # Capture the output
        captured = capsys.readouterr()
        # Validate the output
        assert "##################################################" in captured.out