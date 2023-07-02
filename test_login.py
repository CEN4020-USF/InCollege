import pytest
import MainMenu
from Pages import LoginPage
from Util import db_helper as db


class TestMenu:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()


    # Sign-in Functionality Unit Tests
    def test_sign_in_valid_credentials(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["john", "Password123", '16']
        if len(inputs) > 0:
            monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Welcome john!" in captured.out

    def test_sign_in_invalid_username(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["unknown", "password123", "15"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return None (no user found)
        with mocker.patch.object(db, 'get_user', return_value=None):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "no user was found with the username unknown" in captured.out


    def test_sign_in_invalid_password(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["john", "wrongpassword", "15"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with different password
        user = ["john", "password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Invalid Password" in captured.out

    def test_create_account_more_than_10_users(self, monkeypatch, capsys, mocker):

        inputs = ["15"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        with mocker.patch.object(db, 'count_users', return_value=11):
            self.login.create_account()

        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "We are not creating new accounts at this time. Please Sign in to existing account" in captured.out


    def test_create_account_existing_user(self, monkeypatch, capsys, mocker):
        inputs = ["TestFirst", "15"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["TestFirst", "Test"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Sorry, this account already exists. Please try again" in captured.out


    def test_create_account_invalid_pass_more_than_12_char(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "ThisIsAVeryLongPass!1", "ValidP@ss1",  "TestFirst", "TestLast", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out


    def test_create_account_invalid_pass_less_than_8_char(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "Short1!", "ValidP@ss1", "TestFirst", "TestLast", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_invalid_pass_all_lowercase(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "lowercase1!", "ValidP@ss1", "TestFirst", "TestLast", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_invalid_pass_no_special_character(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "NoSpecial1", "ValidP@ss1", "TestFirst", "TestLast", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_invalid_pass_no_numbers(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "NoNumbers!", "ValidP@ss1", "TestFirst", "TestLast", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_valid(self, mocker, capsys, monkeypatch):
        inputs = ["TestUserValid", "ValidP@ss1", "First", "Last", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Sending you to the main menu navigation" in captured.out

    def test_create_account_University_valid_input(self, mocker, capsys, monkeypatch):
        inputs = ["TestUserValid", "ValidP@ss1", "First", "Last", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Sending you to the main menu navigation" in captured.out

    def test_create_account_Major_valid_input(self, mocker, capsys, monkeypatch):
        inputs = ["TestUserValid", "ValidP@ss1", "First", "Last", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Sending you to the main menu navigation" in captured.out
