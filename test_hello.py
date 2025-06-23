from application import app


def test_hello_page():
    with app.test_client() as test_client:
        response = test_client.get('/hello')
        assert response.status_code == 200
        assert b"Hello World" in response.data
        assert b"test" in response.data
        assert b"Version" in response.data