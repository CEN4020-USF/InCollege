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

    def test_has_Profile(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        info = ["blanders1", "title" "Computer Engineer"]
        with mocker.patch.object(db, 'set_user_profile', return_value=info):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Benjamin Landers's User Profile" in captured.out

    def test_set_Title(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "1", "Cool Guy", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Title: Cool Guy" in captured.out

    def test_delete_Title(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "1", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Title: " in captured.out

    def test_set_Major(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "2", "Computer Engineer", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Major: Computer Engineer" in captured.out

    def test_delete_Major(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "2", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Major: " in captured.out

    def test_set_University(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "3", "University Of South Florida", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "University: University Of South Florida" in captured.out

    def test_delete_University(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "3", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "University: " in captured.out

    def test_add_about(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "4", "I peaked in highschool", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "About: \nI peaked in highschool" in captured.out

    def test_change_about(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "4", "I took a correspondance course", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "About: \nI took a correspondance course" in captured.out

    def test_delete_about(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "4", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "About: \n" in captured.out

    def test_no_experience(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "There is no relevant professional experience yet" in captured.out

    def test_has_experience(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "15", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Title"; "Employer"; "Date Started"; "Date Ended"; "Location"; "Description" in captured.out

    def test_add_experience(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "15", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        #add_job( created_by, title, description, employer, location, salary, date_started="", date_ended=""):
        job =["rmalloy1", "test", "test", "test", "test", "test", "test", "test",]
        with mocker.patch.object(db, "add_job", return_value=job):
            self.login.menu()
        

        captured = capsys.readouterr()

        # Validate the output
        assert "Title"; "Employer"; "Date Started"; "Date Ended"; "Location"; "Description"; "test"; "test"; "test"; "test"; "test" in captured.out

    def test_no_education(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "There is no relevant education experience yet" in captured.out

    def test_add_education(self, monkeypatch, capsys, mocker):
        inputs = ["11", "rmalloy1", "Password1!", "15", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        #add_education(username, school, degree, start, end):
        job =["rmalloy1", "test", "test", "test", "test"]
        with mocker.patch.object(db, "add_education", return_value=job):
            self.login.menu()
        

        captured = capsys.readouterr()

        # Validate the output
        assert "School"; "Degree"; "Start Year"; "End Year"; "test"; "test"; "test"; "test" in captured.out
    
    def test_quit_mid_title(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "1", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Thank you for using inCollege" in captured.out

    def test_save_and_change_title(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "1", "brooskie", "0", "1", "1", "Literal CHAD", "0", "1", "1", "", "0","0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Title: brooskie"; "Title: Literal CHAD" in captured.out

    def test_quit_mid_major(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "2", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Thank you for using inCollege" in captured.out

    def test_save_and_change_major(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "2", "Brooskie", "0", "1", "2", "Literal Chad", "0", "1", "2", "", "0","0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Title: Brooskie"; "Title: Literal Chad" in captured.out

    def test_quit_mid_University(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "2", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Thank you for using inCollege" in captured.out

    def test_save_and_change_University(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "3", "Brooskie University", "0", "1", "3", "Chad University", "0", "1", "3", "", "0","0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Title: Brooskie University"; "Title: Chad University" in captured.out

    def test_quit_mid_About(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "4", "", "0", "0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Thank you for using inCollege" in captured.out

    def test_save_and_change_About(self, monkeypatch, capsys, mocker):
        inputs = ["11", "blanders1", "Password1!", "15", "1", "4", "I peaked in highschool", "0", "1", "4", "I took a correspondance course", "0", "1", "4", "", "0","0", '16']
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        with mocker.patch.object(db, 'check_name', return_value=None):
            self.login.menu()
        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Title: I peaked in highschool"; "Title: I took a correspondance course" in captured.out
    

    