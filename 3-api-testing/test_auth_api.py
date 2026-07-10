import pytest

BASE_URL = "https://reqres.in/api"


class TestAuthAPI:

    def test_login_success(self, api_session):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = api_session.post(f"{BASE_URL}/login", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert data["token"] == "QpwL5tke4Pnpja7X4"

    def test_login_missing_password(self, api_session):
        payload = {
            "email": "eve.holt@reqres.in"
        }
        response = api_session.post(f"{BASE_URL}/login", json=payload)

        assert response.status_code == 400
        data = response.json()
        assert "error" in data
        assert data["error"] == "Missing password"

    def test_login_missing_email(self, api_session):
        payload = {
            "password": "cityslicka"
        }
        response = api_session.post(f"{BASE_URL}/login", json=payload)

        assert response.status_code == 400
        data = response.json()
        assert "error" in data
        assert data["error"] == "Missing email or username"

    def test_login_user_not_found(self, api_session):
        payload = {
            "email": "notfound@reqres.in",
            "password": "whatever"
        }
        response = api_session.post(f"{BASE_URL}/login", json=payload)

        assert response.status_code == 400
        data = response.json()
        assert "error" in data

    def test_register_success(self, api_session):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = api_session.post(f"{BASE_URL}/register", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["id"] == 4
        assert "token" in data

    def test_register_missing_password(self, api_session):
        payload = {
            "email": "sydney@fife"
        }
        response = api_session.post(f"{BASE_URL}/register", json=payload)

        assert response.status_code == 400
        data = response.json()
        assert "error" in data
        assert data["error"] == "Missing password"
