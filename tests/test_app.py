from app import app

def test_home_route():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert data["ok"] is True
    assert "CI" in data["msg"]
