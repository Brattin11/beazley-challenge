# Import sys module for modifying Python's runtime environment
import sys
# Import os module for interacting with the operating system
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app instance from the main app file
from app import app 
# Import pytest for writing and running tests
import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_get(client):
    """Test the get route."""
    response = client.get('/api/data')
    assert response.status_code == 200

def test_post(client):
    body = {"443": "nginx"}
    postResponse = client.post('/api/data/create', json=body)
    assert postResponse.status_code == 201

    getResponse = client.get('/api/data')
    assert getResponse.json == [body]

def test_put(client):
    body = {"443": "nginx2"}

    notFoundResponse = client.put('/api/data/update/444', json=body)
    assert notFoundResponse.status_code == 404

    successResponse = client.put('/api/data/update/443', json=body)
    assert successResponse.status_code == 200

    getResponse = client.get('/api/data')
    assert getResponse.json == [body]

def test_delete(client):
    notFoundResponse = client.delete('api/data/delete/444')
    assert notFoundResponse.status_code == 404

    successResponse = client.delete('api/data/delete/443')
    assert successResponse.status_code == 200

    getResponse = client.get('/api/data')
    assert getResponse.json == []
    
