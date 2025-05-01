import requests
import pytest

def test_getmethod():
    id = '3560'
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    response_body = requests.get(full_url)
    assert response_body.status_code == 200
    data = response_body.json()
    print(data)
    assert 'firstname' in data, " firstname is not present"
    assert 'lastname' in data, "Lastname is not present"
    # assert 'address' in data, "address is not present"

    assert data['firstname'] == 'Jim', "Incorrect First name"
    assert data['lastname'] == 'Brown', "Incorrect Last name"