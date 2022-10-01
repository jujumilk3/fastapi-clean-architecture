def test_client(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "service is working"
