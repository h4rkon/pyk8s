

def test_get(client):

    # act
    login_response = client.post(
        '/token/',
        data={'grant_type': 'password',
              'username': 'johndoe',
              'password': 'secret'}).json()
    headers = {
        'Authorization':
            f'{login_response["token_type"]} {login_response["access_token"]}'}
    response = client.get('/greetings/', headers=headers)
    print(response.status_code)

    # assert
    assert response.status_code == 200
    assert "username='johndoe'" in response.text
