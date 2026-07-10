import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    return session
