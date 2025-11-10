import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_home_page(client):
    """Verify that the home (login) page loads and contains title text."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Study Calendar' in rv.data
