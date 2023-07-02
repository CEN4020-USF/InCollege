import pytest
import MainMenu
from Pages import LoginPage
from Pages import ConnectionsPage
from Pages import UserProfilePage
from Util import db_helper as db

class Testprofile:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()
        self.connections = ConnectionsPage.ConnectionsPage()
        self.profile = UserProfilePage.UserProfilePage()

    def test_User_Has_Profile(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "15", "0", "16"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()   
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "* Robert Malloy's User Profile *" in captured.out

    def test_User_No_Profile(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "15", "0", "16"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()   
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "There is no relevant professional experience yet." in captured.out

    def test_Friend_No_Profile(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "15", "2", "1", "test_user", "0", "16"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()   
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Looks like the user you are trying to connect to either: 1.) Is not a friend or 2.) Does not have a profile set up" in captured.out
    
    def test_Friend_Has_Profile(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "15", "2", "1", "rmalloy1", "0", "0", "0", "16"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()   
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "* Robert Malloy's User Profile *" in captured.out

    def test_Invalid_Input_Profile(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "15", "blank","0", "16"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()   
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "is not a valid response" in captured.out

    def test_Invalid_Input_Friends(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "15", "2", "blank","0", "0", "16"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()   
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "is not a valid choice" in captured.out