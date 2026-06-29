from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "URL Shortener API is running"}

def test_shorten_url_valid():
    response = client.post("/shorten", json={"url": "https://www.google.com"})
    assert response.status_code == 200
    assert "short_code" in response.json()
    assert response.json()["short_code"] is not None

def test_post_shorten_url_invalid():
    response = client.post("/shorten", json={"url": "invalid_url"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid URL"}

def test_redirect_to_url():
    response = client.post("/shorten", json={"url": "https://www.google.com"})
    assert response.status_code == 200
    assert "short_code" in response.json()
    code = response.json()["short_code"]

    response = client.get(f"/{code}", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://www.google.com"

def test_redirect_to_non_existent_url():
    response = client.get("/nonexistent_code")
    assert response.status_code == 404
    assert response.json() == {"detail": "Short code not found"}
