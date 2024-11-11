import requests

url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data[0],'\n')
    print('Name : ',data[0]['name'])
    print('Email: ',data[0]['email'])
else:
    print("Bad request: ",response.status_code)
    