# This Python code snippet is performing the following actions:
# This Python code snippet is making a GET request to the URL "https://jsonplaceholder.typicode.com/users" using the `requests` library. It then checks if the response status code is 200 (indicating a successful request), and if so, it converts the response data to JSON format.
import requests

url="https://jsonplaceholder.typicode.com/users"

response=requests.get(url)

if response.status_code==200:
    data=response.json()
    print(data[0],'\n')
    for key,value in data[0].items():
        print(key,' : ',value,'\n')
    print('Name : ',data[0]['name'])
    print('Email : ',data[0]['email'])
    print('City : ',data[0]['address']['city'])
else:
    print("Bad request : ",response.status_code)