import requests
import pytest


def test_postmethod():
    # url
    url = "https://restful-booker.herokuapp.com/booking"
    json = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    header = {"Content-Type": "application/json"}
    response = requests.post(url=url, json=json, auth=None, headers=header)
    data = response.json()
    booking_id = response.json()['bookingid']
    print(data)
    print(booking_id)
    assert response.status_code == 200, 'Expected status code is 200'
