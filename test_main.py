from main import ping, app

status_ok = 200

def test_ping():
    assert ping() == "ping"

def test_ping_endpoint():
    client = app.test_client()
    actual = client.get("/ping")
    assert actual.status_code == status_ok
