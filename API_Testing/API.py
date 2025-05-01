import requests


def main():
    url = "https://restful-booker.herokuapp.com/booking/646"
    response_body = requests.get(url)
    print(response_body.status_code)
    assert response_body.status_code == 200, 'wrong status code'
    print(response_body.json())

if __name__ == '__main__':
    main()
