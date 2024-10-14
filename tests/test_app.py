import pytest
from flask import json

@pytest.fixture
def client():
    from app.app import create_app
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

def test_ask_question(client, mocker):
    # Example question to send
    test_question = {"question": "What is the capital of Israel? write one word only."}

    # Create a mock for the OpenAIService instance
    mock_openai_service = mocker.patch('app.services.OpenAIService')
    instance = mock_openai_service.return_value  # Get the instance of the mock

    # Mocking the get_answer_from_openai method
    instance.get_answer_from_openai.return_value = "Jerusalem"  # Mocked response

    # Making the POST request to /ask
    response = client.post('/ask', json=test_question)

    # Checking the response status code and content
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['question'] == test_question['question']
    assert data['answer'] == "Jerusalem"

def test_ask_invalid_input(client):
    # Testing the /ask route with an invalid input (no 'question' key)
    response = client.post('/ask', json={"wrong_key": "value"})
    
    # It should return a 400 Bad Request
    assert response.status_code == 400

    # Checking the error message
    data = json.loads(response.data)
    assert "Invalid input" in data['error']

