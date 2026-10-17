from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"End-to-End DevOps Pipeline Lab 10" in response.data

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data
