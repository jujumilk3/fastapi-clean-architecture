def test_sign_up_and_sign_in(client):
    response = client.post(
        "/api/v1/auth/sign-up",
        json={"email": "test", "password": "test", "name": "test"},
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["email"] == "test"
    assert response_json["name"] == "test"
    assert response_json["id"] > 0
    user_token = response_json["user_token"]

    response = client.post(
        "/api/v1/auth/sign-in",
        json={"email__eq": "test", "password": "test"},
    )

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["user_info"]["email"] == "test"
    assert response_json["user_info"]["name"] == "test"
    assert response_json["user_info"]["id"] > 0
    assert response_json["user_info"]["user_token"] == user_token
    assert response_json["access_token"] is not None
