import requests

def main():
    url = "https://restful-booker.herokuapp.com/booking/"
    id = '23'
    full_url = url + id
    a = requests.get(full_url)
    print(f'text is {a.text} and status code is {a.status_code}')
    assert a.status_code == 200




if __name__ == "__main__":
    main()