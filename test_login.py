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
        inputs = ["john", "Password123", "4"]
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
        inputs = ["unknown", "password123", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return None (no user found)
        with mocker.patch.object(db, 'get_user', return_value=None):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "no user was found with the username unknown" in captured.out


    def test_sign_in_invalid_password(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["john", "wrongpassword", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with different password
        user = ["john", "password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Invalid Password" in captured.out

    def test_create_account_more_than_5_users(self, monkeypatch, capsys, mocker):

        inputs = ["5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        with mocker.patch.object(db, 'count_users', return_value=6):
            self.login.create_account()

        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "We are not creating new accounts at this time. Please Sign in to existing account" in captured.out


    def test_create_account_existing_user(self, monkeypatch, capsys, mocker):
        inputs = ["Robert Malloy", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["Robert Malloy", "password"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Sorry, this account already exists. Please try again" in captured.out


    def test_create_account_invalid_pass_more_than_12_char(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "ThisIsAVeryLongPass!1", "ValidP@ss1", "TestFirst", "TestLast",  "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out


    def test_create_account_invalid_pass_less_than_8_char(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "Short1!", "ValidP@ss1", "TestFirst", "TestLast",  "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_invalid_pass_all_lowercase(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "lowercase1!", "ValidP@ss1", "TestFirst", "TestLast",  "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_invalid_pass_no_special_character(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "NoSpecial1", "ValidP@ss1", "TestFirst", "TestLast",  "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_invalid_pass_no_numbers(self, monkeypatch, capsys, mocker):
        inputs = ["TestUserInvalid", "NoNumbers!", "ValidP@ss1", "TestFirst", "TestLast",  "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_create_account_valid(self, mocker, capsys, monkeypatch):
        inputs = ["TestUserValid", "ValidP@ss1", "First", "Last", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Sending you to the main menu navigation" in captured.out

    def test_video_playing(self, mocker, capsys, monkeypatch):
        inputs = ["4", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "get_user"):
            self.login.play_video()

        captured = capsys.readouterr()
        assert "* Video is now playing *" in captured.out

    def test_create_account_valid_first_last(self, mocker, capsys, monkeypatch):
        inputs = ["TestUserValid", "ValidP@ss1", "cool", "sick", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "add_user"):
            self.login.create_account()

        captured = capsys.readouterr()
        assert "Welcome TestUserValid!" in captured.out

    def test_search_for_someone_valid(self, mocker, capsys, monkeypatch):
        inputs = ["3", "1", "ben", "land", "2", "2", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "get_user"):
            self.login.search()

        captured = capsys.readouterr()
        assert "\nThey are part of the InCollege system\n" in captured.out

    def test_search_for_someone_invalid(self, mocker, capsys, monkeypatch):
        inputs = ["3", "1", "fake", "name", "2", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, "get_user"):
            self.login.search()

        captured = capsys.readouterr()
        assert "\nThey are not yet a part of the InCollege system yet\n" in captured.out

    def test_search_for_someone_valid_login(self, mocker, capsys, monkeypatch):
        inputs = ["3", "1", "ben", "land", "1", "1", "blanders1", "Forgaming1!", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["blanders1", "Forgaming1!"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.search()

        captured = capsys.readouterr()
        assert "Welcome blanders1!" in captured.out

    def test_search_for_someone_invalid_login(self, mocker, capsys, monkeypatch):
        inputs = ["3", "1", "ben", "land", "1", "1", "notreal", "Forgaming1!", "5", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'get_user', return_value=None):
            self.login.search()

        captured = capsys.readouterr()
        assert "\nUnfortunately, no user was found with the username notreal.\n" in captured.out

    def test_search_for_someone_valid_create_user_valid(self, mocker, capsys, monkeypatch):
        inputs = ["3", "1", "ben", "land", "1", "2", "TestUserValid", "ValidP@ss1", "cool", "sick", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'add_user'):
            self.login.search()

        captured = capsys.readouterr()
        assert "Welcome TestUserValid!" in captured.out
    
    def test_search_for_someone_valid_create_user_invalid_less_than_8_chars(self, mocker, capsys, monkeypatch):
        inputs = ["3", "1", "ben", "land", "1", "2", "TestUserValid", "P@ss1", "ValidP@ss1", "cool", "sick", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'add_user'):
            self.login.search()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out


    def test_search_for_someone_valid_create_user_invalid_existing_user(self, monkeypatch, capsys, mocker):
        inputs = ["3", "1", "ben", "land", "1", "2", "blanders1", "5"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'add_user'):
            self.login.search()

        captured = capsys.readouterr()
        assert "Sorry, this account already exists. Please try again" in captured.out


    def test_search_for_someone_valid_create_user_invalid_more_than_12_char(self, monkeypatch, capsys, mocker):
        inputs = ["3", "1", "ben", "land", "1", "2", "TestUserValid", "longpassValidP@ss1", "ValidP@ss1", "cool", "sick", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'add_user'):
            self.login.search()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_search_for_someone_valid_create_user_invalid_pass_all_lowercase(self, monkeypatch, capsys, mocker):
        inputs = ["3", "1", "ben", "land", "1", "2", "TestUserValid", "lowercase1!", "ValidP@ss1", "cool", "sick", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'add_user'):
            self.login.search()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_search_for_someone_valid_create_user_invalid_pass_no_special_character(self, monkeypatch, capsys, mocker):
        inputs = ["3", "1", "ben", "land", "1", "2", "TestUserValid", "NoSpecial1", "ValidP@ss1", "cool", "sick", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'add_user'):
            self.login.search()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out

    def test_search_for_someone_valid_create_user_invalid_pass_no_numbers(self, monkeypatch, capsys, mocker):
        inputs = ["3", "1", "ben", "land", "1", "2", "TestUserValid", "NoNumbers!", "ValidP@ss1", "cool", "sick", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'add_user'):
            self.login.search()

        captured = capsys.readouterr()
        assert "Invalid password please try again: " in captured.out
