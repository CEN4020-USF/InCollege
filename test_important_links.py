import pytest
import MainMenu
from Pages import LoginPage

from Util import db_helper as db


class TestUsefulLinks:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()

    def test_navigation_copyright_notice(self, monkeypatch, capsys, mocker):
        inputs = ['31', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Team New Mexico" in captured.out

    def test_navigation_about(self, monkeypatch, capsys, mocker):
        inputs = ['32', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "InCollege is designed to be an alternative" in captured.out

    def test_navigation_accessibility(self, monkeypatch, capsys, mocker):
        inputs = ['33', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Accessibility Statement" in captured.out

    def test_navigation_user_agreement(self, monkeypatch, capsys, mocker):
        inputs = ['34', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "User Agreement:" in captured.out

    def test_navigation_cookie_policy(self, monkeypatch, capsys, mocker):
        inputs = ['35', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Our site uses essential cookies" in captured.out

    def test_navigation_copyright_policy(self, monkeypatch, capsys, mocker):
        inputs = ['36', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Copyright Policy:" in captured.out

    def test_navigation_brand_policy(self, monkeypatch, capsys, mocker):
        inputs = ['37', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "**InCollege Brand Usage Guidelines**" in captured.out

    def test_navigation_language_not_logged_in(self, monkeypatch, capsys, mocker):
        inputs = ['39', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Please login before trying to edit language settings" in captured.out

    def test_navigation_language_loggin_in(self, monkeypatch, capsys, mocker):
        inputs = ["11", "test", "Password1!", "39", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        info = ["blanders1", "title" "Computer Engineer"]
        with mocker.patch.object(db, 'set_user_profile', return_value=info):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "* Language *" in captured.out

    def test_navigation_language_change_english(self, monkeypatch, capsys, mocker):
        inputs = ['39', '1', '16', 16]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["test", "Password123", "first", "last", "1", "1", "1", "English"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=True):
            with mocker.patch.object(db, 'get_user', return_value=user):
                with mocker.patch.object(db, 'change_language'):
                    with mocker.patch.object(db, "get_pending_from", return_value=None):
                        self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Your language has been set to English!" in captured.out

    def test_navigation_language_change_spanish(self, monkeypatch, capsys, mocker):
        inputs = ['39', '2', '16', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["test", "Password123", "first", "last", "1", "1", "1", "English"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=True):
            with mocker.patch.object(db, 'get_user', return_value=user):
                with mocker.patch.object(db, 'change_language'):
                    with mocker.patch.object(db, "get_pending_from", return_value=None):
                        self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Your language has been set to Spanish!" in captured.out


    def test_navigation_privacy_policy_not_logged_in(self, monkeypatch, capsys, mocker):
        inputs = ['38', '1', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'is_user_signed_in', return_value=False):
            self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Please sign in to edit settings" in captured.out

    def test_navigation_privacy_policy_logged_in(self, monkeypatch, capsys, mocker):
        inputs = ['38', '1', '4', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["test", "Password123", "first", "last", "1", "1", "1", "English"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=True):
            with mocker.patch.object(db, 'get_user', return_value=user):
                self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "* Guest Controls Page *" in captured.out

    def test_navigation_privacy_policy_toggle_email(self, monkeypatch, capsys, mocker):
        inputs = ['38', '1', '1', '4', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["test", "Password123", "first", "last", "1", "1", "1", "English"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=True):
            with mocker.patch.object(db, 'get_user', return_value=user):
                with mocker.patch.object(db, 'toggle_email'):
                    self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Email Notifications Updated" in captured.out

    def test_navigation_privacy_policy_toggle_sms(self, monkeypatch, capsys, mocker):
        inputs = ['38', '1', '2', '4', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["test", "Password123", "first", "last", "1", "1", "1", "English"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=True):
            with mocker.patch.object(db, 'get_user', return_value=user):
                with mocker.patch.object(db, 'toggle_sms'):
                    self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "SMS Notifications Updated" in captured.out

    def test_navigation_privacy_policy_toggle_advertising(self, monkeypatch, capsys, mocker):
        inputs = ['38', '1', '3', '4', '0', '15']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        user = ["test", "Password123", "first", "last", "1", "1", "1", "English"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=True):
            with mocker.patch.object(db, 'get_user', return_value=user):
                with mocker.patch.object(db, 'toggle_advertising'):
                    self.login.menu()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Targeted Advertising Updated" in captured.out

    