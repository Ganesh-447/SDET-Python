import pytest
import requests
def test_1():
    assert 9 == 9
def test_3():
    assert  9 == 8

def test_get():
    id = '244'
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    response_body = requests.get(full_url)
    assert response_body.status_code == 200
    data = response_body.json()
    print(data)
    assert 'firstname' in data, " firstname is not present"
    assert 'lastname' in data, "Lastname is not present"
    # assert 'address' in data, "address is not present"

    assert data['firstname'] == 'Josh', "Incorrect First name"
    assert data['lastname'] == 'Allen', "Incorrect Last name"
    assert data['bookingdates']['checkin'] == '2018-01-01', "Incorrect checkin dates"

