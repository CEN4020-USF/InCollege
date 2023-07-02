import pytest
import MainMenu
from Pages import LoginPage
from Util import db_helper as db


class TestNavigation:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()

    def test_navigation_to_job_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "13", "9", '16', '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "1.) Post a job" in captured.out

    def test_navigation_to_connections_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "12", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "1.) Search by Last Name" in captured.out

    def test_navigation_to_skills_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "11", "9", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Please Select a Skill" in captured.out

    def test_navigation_to_skill1_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "11", "1", "9", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_to_skill2_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "11", "2", "9", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123", "4"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_to_skill3_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "11", "3", "9" ,'16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_to_skill4_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "11", "4", "9", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out

    def test_navigation_to_skill5_page(self, monkeypatch, capsys, mocker):
        inputs = ["john", "Password123", "11", "5", "9", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out
