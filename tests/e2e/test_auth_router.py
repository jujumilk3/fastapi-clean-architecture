def test_sign_up(client):
    response = client.post(
        "/api/v1/auth/sign-up",
        json={"email": "test", "password": "test", "name": "test"},
    ).json()
    print(response)
    assert False
