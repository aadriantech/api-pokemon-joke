import pytest
from flask import Flask, json
from app.controllers.PokeJokeController import PokeJokeController
from unittest.mock import Mock

# Mock the `requests.get` function
@pytest.fixture
def mock_requests_get(mocker):
    mock_get = mocker.patch('app.controllers.PokeJokeController.requests.get')
    return mock_get

# Mock Flask's request object
@pytest.fixture
def mock_request(mocker):
    mock = mocker.patch('flask.request.args.get')
    return mock

def test_fetch_joke_single_type(mock_requests_get):
    # Mock the response from the joke API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "type": "single",
        "joke": "This is a single joke."
    }
    mock_requests_get.return_value = mock_response
    
    controller = PokeJokeController()
    joke = controller.fetch_joke()
    
    assert joke == "This is a single joke."    

def test_fetch_joke_two_part_type(mock_requests_get):
    # Mock the response from the joke API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "type": "twopart",
        "setup": "Why did the chicken cross the road?",
        "delivery": "To get to the other side."
    }
    mock_requests_get.return_value = mock_response
    
    controller = PokeJokeController()
    joke = controller.fetch_joke()
    
    assert joke == "Why did the chicken cross the road? To get to the other side."

def test_fetch_joke_failure(mock_requests_get):
    # Mock a failed response from the joke API
    mock_response = Mock()
    mock_response.status_code = 404
    mock_requests_get.return_value = mock_response
    
    controller = PokeJokeController()
    joke = controller.fetch_joke()
    
    assert joke is None

def test_fetch_pokemon_skills_success(mock_requests_get):
    # Simulate a successful response from the API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "moves": [
            {"move": {"name": "tackle"}},
            {"move": {"name": "thunderbolt"}}
        ]
    }
    mock_requests_get.return_value = mock_response
    
    instance = PokeJokeController()
    skills = instance.fetch_pokemon_skills("pikachu")
    
    assert skills == ["tackle", "thunderbolt"]

def test_fetch_pokemon_skills_failure(mock_requests_get):
    # Simulate a non-200 response from the API
    mock_response = Mock()
    mock_response.status_code = 404
    mock_requests_get.return_value = mock_response
    
    instance = PokeJokeController()
    skills = instance.fetch_pokemon_skills("pikachu")
    
    assert skills is None

