import requests
import pytest


# get method. needs URL with booking id, verify status code
# and data(verify firstname field present  and first name is matching or not)
def test_getmethod():
    url = "https://restful-booker.herokuapp.com/booking/"
    id = postmethod()
    URL = url + str(id)
    response_body = requests.get(url=URL)
    data = response_body.json()
    print(data)
    assert response_body.status_code == 200, 'not successfull'
    assert 'firstname' in data, 'first name is not present'
    assert 'lastname' in data, 'last name is not present'
    assert data['firstname'] == 'Jim', 'firstname is not matching'
    assert data['lastname'] == 'Brown', 'lastname is not matching'
    assert data['bookingdates']['checkin'] == "2018-01-01", 'checking is not matching'


# post method need - url,header,payload
def postmethod():
    URL = "https://restful-booker.herokuapp.com/booking"
    Header = {"Content-Type": "application/json"}
    Json = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_body = requests.post(url=URL, headers=Header, json=Json)
    data = response_body.json()
    print(data)
    booking_id = data['bookingid']
    print(f'bookingid is {booking_id}')
    assert response_body.status_code == 200, 'unsucessful request'
    assert data['bookingid'] is not None
    assert data['booking']['firstname'] == 'Jim', 'firstname not matched'
    assert data['booking']['lastname'] == 'Brown', 'lastname not matched'
    assert data['booking']['totalprice'] == 111
    return booking_id


# token generation is done by post method, needs url and payload(json)
def token_creation():
    url = "https://restful-booker.herokuapp.com/auth"
    #header = {"Content-Type":'applicaiton/json'}
    Json = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, json=Json)
    data = response.json()
    token = data['token']
    print(token)
    assert response.status_code == 200
    return token


# put need, url,header(contenttype,cookie),json.
def test_put():
    url = 'https://restful-booker.herokuapp.com/booking/'
    id = postmethod()
    URL = url + str(id)
    Cookie_value = 'token='+token_creation()
    Headers = {'Content-Type': 'application/json',
               'Cookie': Cookie_value
               }
    Json = {
        "firstname": "Ganesh",
        "lastname": "G",
        "totalprice": 987,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_body = requests.put(url=URL,headers=Headers,json=Json)
    data = response_body.json()
    print(data)
    assert response_body.status_code == 200,'request unsucessful'
    assert 'firstname' in data, 'first name is not present'
    assert 'lastname' in data, 'last name is not present'
    assert data['firstname'] == 'Ganesh', 'firstname is not matching'
    assert data['lastname'] == 'G', 'lastname is not matching'
    assert data['bookingdates']['checkin'] == "2018-01-01", 'checking is not matching'

def test_deletemethod():
    id = postmethod()
    url ='https://restful-booker.herokuapp.com/booking/'
    Cookie_value = 'token='+token_creation()
    header = {'Content-Type': 'application/json',
               'Cookie': Cookie_value}
    URL = url + str(id)
    response_body = requests.delete(url=URL,headers=header)
    assert response_body.status_code == 201 , 'deletion unsuccessful'


