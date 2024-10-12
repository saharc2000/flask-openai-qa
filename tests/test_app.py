import pytest
from app import create_app, db

#need improvement
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_ask_question(client):
    response = client.post('/ask', json={'question': 'What is Python?'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'question' in data
    assert 'answer' in data