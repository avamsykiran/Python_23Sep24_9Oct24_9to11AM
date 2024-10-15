import requests

url = "https://jsonplaceholder.typicode.com/users"

resp = requests.get(url)

if resp.ok:
    print(resp.json())
else:
    if resp.status_code==404:
        print("Resource Requested Is Not Found")
    elif resp.status_code==400:
        print("Bad Request")
    else:
        print(resp.status_code)
