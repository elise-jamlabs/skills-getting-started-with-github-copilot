import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    # Arrange
    # (No special setup needed for root endpoint)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    # Optionally, check response content
    # assert response.json() == {"message": "Hello World"}

def test_get_activities():
    # Arrange
    # (No special setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Chess Club" in response.json()

def test_signup_and_unregister():
    # Arrange
    activity = "Chess Club"
    email = "student@example.com"
    # Ensure clean state
    from src.app import activities
    activities[activity]["participants"] = []

    # Act: signup
    signup_response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert: signup
    assert signup_response.status_code == 200
    assert email in activities[activity]["participants"]

    # Act: unregister
    unregister_response = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert: unregister
    assert unregister_response.status_code == 200
    assert email not in activities[activity]["participants"]
