import pytest
import MainMenu
from Pages import LoginPage
from Pages import ConnectionsPage
from Util import db_helper as db


class profile:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()
        self.connections = ConnectionsPage.ConnectionsPage()

    #def test_has_title(self, monkeypatch, capsys, mocker):
    #    inputs = ["11", "blanders1", "Forgaming1!", "15", "0", 16]
    #    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    #    info = ["blanders1", "title" "Computer Engineer"]
    #    with mocker.patch.object(db, 'set_user_profile', return_value=info):
    #        self.login.menu()
        # Capture the output
    #    captured = capsys.readouterr()

    #    # Validate the output
    #    assert "Computer Engineer" in captured.out