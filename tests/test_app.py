

def test_get_greetings(client):

    # act
    response = client.get('/greetings/')

    # assert
    assert response.status_code == 200
    assert "Hello World!" in response.text


def test_get_else(client):
    # act
    response = client.get('/notthere/')

    # assert
    assert response.status_code == 404
