import pytest

BASE_URL = "https://reqres.in/api"


class TestUsersAPI:

    def test_get_users_page1(self, api_session):
        response = api_session.get(f"{BASE_URL}/users", params={"page": 1})

        assert response.status_code == 200
        data = response.json()
        assert data["page"] == 1
        assert "data" in data
        assert len(data["data"]) > 0
        assert "id" in data["data"][0]
        assert "email" in data["data"][0]
        assert "first_name" in data["data"][0]
        assert "last_name" in data["data"][0]

    def test_get_single_user(self, api_session):
        response = api_session.get(f"{BASE_URL}/users/2")

        assert response.status_code == 200
        data = response.json()
        assert data["data"]["id"] == 2
        assert data["data"]["email"] == "janet.weaver@reqres.in"
        assert data["data"]["first_name"] == "Janet"
        assert data["data"]["last_name"] == "Weaver"

    def test_get_user_not_found(self, api_session):
        response = api_session.get(f"{BASE_URL}/users/23")

        assert response.status_code == 404

    def test_create_user(self, api_session):
        payload = {
            "name": "Zhang San",
            "job": "QA Engineer"
        }
        response = api_session.post(f"{BASE_URL}/users", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Zhang San"
        assert data["job"] == "QA Engineer"
        assert "id" in data
        assert "createdAt" in data

    def test_update_user_put(self, api_session):
        payload = {
            "name": "Zhang San Updated",
            "job": "Senior QA Engineer"
        }
        response = api_session.put(f"{BASE_URL}/users/2", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Zhang San Updated"
        assert data["job"] == "Senior QA Engineer"
        assert "updatedAt" in data

    def test_update_user_patch(self, api_session):
        payload = {
            "job": "Lead QA Engineer"
        }
        response = api_session.patch(f"{BASE_URL}/users/2", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["job"] == "Lead QA Engineer"

    def test_delete_user(self, api_session):
        response = api_session.delete(f"{BASE_URL}/users/2")

        assert response.status_code == 204

    def test_users_response_time(self, api_session):
        response = api_session.get(f"{BASE_URL}/users", params={"page": 1})

        assert response.elapsed.total_seconds() < 5

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
    def test_multiple_user_ids_return_200(self, api_session, user_id):
        response = api_session.get(f"{BASE_URL}/users/{user_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["data"]["id"] == user_id
