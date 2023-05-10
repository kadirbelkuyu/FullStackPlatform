import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app.test_client()

def test_hello(app):
    response = app.get('/hello')
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello, World!"
