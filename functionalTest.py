import pytest
import requests
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")


BASE_URL = "http://localhost:5000"  # Update with your smart home system URL

def test_user_login():
    response = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "admin123"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_device_control():
    token = "your_auth_token"  # Replace with an actual token after login
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.post(f"{BASE_URL}/control", json={"device": "light", "state": "on"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_automation_rule():
    response = requests.get(f"{BASE_URL}/rules")
    assert response.status_code == 200
    assert "rules" in response.json()

