# test_app.py
import pytest
from app import app as flask_app  # Import the Flask app from app.py

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello,world!'  # Adjust this assertion based on your app's response

