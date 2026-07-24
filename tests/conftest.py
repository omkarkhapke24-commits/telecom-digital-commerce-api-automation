#conftest file prepares objects (awa test data, db connectn, browers, temporary files, clean up) for tests. therefore, fixtures belong here.

import pytest
from utils.api_client import APIClient
from config.credentials import LOGIN_CREDENTIALS
from apis.user_api import UserAPI
from config.current_environment import CURRENT_ENV
from config.config import BASE_URL


@pytest.fixture #ka decorator #creates a centralised object that allows class attributes to be accessed directly by other code files/tests
def api_client(): 
    return APIClient() #APIClient()? It's an object (instance) of the APIClient class.

#5-6:"This isn't just any function.
#  This is a fixture.
#  You may use it to provide objects to tests."

@pytest.fixture
def authenticated_api_client(api_client):
    # Log in once and provide an authenticated client to tests.
    api_client.login(LOGIN_CREDENTIALS)
    return api_client

@pytest.fixture
def user_api(api_client):
    return UserAPI(api_client)

# HTML Report Hook
def pytest_html_report_title(report):
    report.title = "Telecom Digital Commerce API Automation Report "

def pytest_metadata(metadata):  #parameter 'metadata' is a dict and follwing lines are we adding k-v pairs to it
    metadata["Environment"]= CURRENT_ENV
    metadata["BASE URL"] = BASE_URL
    metadata["FRAMEWORK"] = "Telecom Digital Commerce API Automation"