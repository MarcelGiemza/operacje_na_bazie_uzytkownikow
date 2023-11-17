from main import *


def test_ping():
    assert ping() == "ping"

def test_ping_endpoint():
    client = app.test_client()
    actual = client.get("/ping")
    assert actual.status_code == OK

def test_post():
    client = app.test_client()
    actual = client.post("/users", json={"name": "test", "lastname": "test"})
    assert actual.status_code == CREATED

def test_pust_wrong():
    client = app.test_client()
    actual = client.post("/users", json={"name": "test"})
    assert actual.status_code == CREATE_WRONG_REQUEST
