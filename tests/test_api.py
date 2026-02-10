from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_gists_for_octocat():
    response = client.get("/octocat")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_pagination():
    response = client.get("/octocat?page=1&per_page=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5

def test_invalid_user():
    response = client.get("/thisuserdoesnotexist123456")
    assert response.status_code == 404
