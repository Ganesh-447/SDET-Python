# import  requests
# url ="https://restful-booker.herokuapp.com/booking/"
# id = '1250'
# total_url = url + id
# response_body = requests.get(total_url)
# data = response_body.json()
# print(data)
# assert response_body.status_code == 200
# assert 'firstname' in data , 'first name is not present'
# assert data['firstname'] == 'Jimr', 'firstname is not matching'

import requests


def main():
    url = "https://restful-booker.herokuapp.com/booking/646"
    response_body = requests.get(url)
    data = response_body.text
    print(data)


main()