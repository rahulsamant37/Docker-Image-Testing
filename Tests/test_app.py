import os
import sys
import pytest
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from src.app import app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello World!'

def test_greet_route(client):
    response = client.get('/greet/John')
    assert response.status_code == 200 
    assert response.data.decode() == 'Hello John!'

def test_greet_route_empty_name(client):
    response = client.get('/greet/')
    assert response.status_code == 404

def test_invalid_route(client):
    response = client.get('/invalid')
    assert response.status_code == 404