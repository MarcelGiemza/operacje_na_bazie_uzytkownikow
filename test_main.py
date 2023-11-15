from main import ping, app

def test_ping():
    assert ping() == "ping"

def test_ping_endpoint():
    client = app.test_client()
    actual = client.get("/ping")
    assert actual.status_code == 200
