import pytest
import requests

@pytest.mark.parametrize("user_id, expected_email", [
    (2, "janet.weaver@reqres.in"),
])
def test_user_data(user_id, expected_email):
    # тест проверяет код ответа получения существующего юзера и наличие data
    # url = f"https://reqres.in/api/users/{user_id}"
    url = f"http://127.0.0.1:8000/api/users/{user_id}"

    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

@pytest.mark.parametrize("user_id, expected_email", [
    (2, "janet.weaver@reqres.in"),
])
def test_response_existing_user_id_and_email(user_id, expected_email):
    # тест проверяет id и почту существующего юзера
    url = f"http://127.0.0.1:8000/api/users/{user_id}"
    response = requests.get(url)
    body = response.json()
    assert "data" in body, "Response body does not contain 'data' key"

    data = body["data"]

    assert data["id"] == user_id, f"Expected id {user_id}, but got {data['id']}"
    assert data["email"] == expected_email, f"Expected email {expected_email}, but got {data['email']}"

@pytest.mark.parametrize("user_id", [
    (3)
])
def test_response_unexisting_user(user_id):
    # тест проверяет код ответа несуществующего юзера
    url = "http://127.0.0.1:8000/api/users/999"

    response = requests.get(url)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"