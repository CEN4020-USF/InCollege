import pytest
import MainMenu
from Pages import LoginPage
from Pages.Useful import BrowseInCollegePage as Browse, DirectoriesPage as Directory, GeneralPage as General, \
    BusinessSolutionsPage as Business

from Util import db_helper as db


class TestUsefulLinks:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()

    def test_navigation_browse_in_college(self, monkeypatch, capsys, mocker):
        inputs = ['22', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_business_solutions(self, monkeypatch, capsys, mocker):
        inputs = ['23', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_directories(self, monkeypatch, capsys, mocker):
        inputs = ['24', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_general_sign_up_already_signed_in(self, monkeypatch, capsys, mocker):
        inputs = ['21', '1', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'is_user_signed_in', return_value=True):
            with mocker.patch.object(db, 'get_user', return_value=user):
                self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "**It seems you are already signed in.**" in captured.out

    def test_navigation_general_help_center(self, monkeypatch, capsys, mocker):
        inputs = ['21', '2', '0', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "We're here to help!" in captured.out

    def test_navigation_general_about(self, monkeypatch, capsys, mocker):
        inputs = ['21', '3', '0', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide." in captured.out

    def test_navigation_general_press(self, monkeypatch, capsys, mocker):
        inputs = ['21', '4', '0', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "In College Pressroom: Stay on top of the latest news, updates, and reports" in captured.out

    def test_navigation_general_blog(self, monkeypatch, capsys, mocker):
        inputs = ['21', '5', '0', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_general_careers(self, monkeypatch, capsys, mocker):
        inputs = ['21', '6', '0', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_general_developers(self, monkeypatch, capsys, mocker):
        inputs = ['21', '7', '0', '0', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "n", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out
