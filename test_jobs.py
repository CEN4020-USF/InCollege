import pytest
import MainMenu
from Pages import LoginPage
from Pages import JobOpportunitiesPage
from Util import db_helper as db


class TestJob:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()
        self.job = JobOpportunitiesPage.JobOpportunitiesPage()


    def test_post_job(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["johnnytest", "Password1!", "13", "1", "Test Title", "Test Desc", "Test Employer", "Test Location", "12345", "9", '16', '16']

        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        # Mocking the get_user method to return a user with matching credentials
        user = ["johnnytest", "Password1!", "John", "Doe"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            with mocker.patch.object(db, 'add_job'):
                self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Job Added" in captured.out


    def test_post_job_prevents_more_than_5_jobs(self, monkeypatch, capsys, mocker):
        inputs = ["4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        with mocker.patch.object(db, 'count_jobs', return_value=6):
            self.job.post_job()

        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "Number of jobs permitted exceeded, going back to main menu" in captured.out

    def test_job_page_returns_to_menu(self, monkeypatch, capsys, mocker):
        inputs = ["9", '16']

        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Run the create_account function
        with mocker.patch.object(db, 'count_jobs', return_value=1):
            self.job.load_job_opportunities()

        # Capture the output
        captured = capsys.readouterr()

        # Validate the output
        assert "1.) Your Skill Development" in captured.out
