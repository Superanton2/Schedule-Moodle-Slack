import requests

url = "https://randomuser.me/api/"

def get_names():
    response = requests.get(url)
    data = response.json()
    lst = data["results"]
    dct = lst[0]
    dct_name = dct["name"]
    first = dct_name["first"]
    last = dct_name["last"]
    print(first, last)
get_names()