import csv

import requests

url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)       


if response.status_code == 200:
    data = response.json()
    
    with open('users.csv', 'w', newline='') as cvsFile:
        fieldNema= ['Name','Email','City']
        writer = csv.DictWriter(cvsFile,fieldnames=fieldNema)
        
        writer.writeheader()
        
        
        for user in data:
            # print('Nema : ',user['name'],'\n','Email : ',user['email'],'\n','City : ',user['address']['city'],'\n')
            print('Name : ',user['name'])
            print('Email : ',user['email'])
            print('City : ',user['address']['city'],)
            print('\n')
            
            writer.writerow(
                {'Name':user['name'],
                'Email':user['email'],
                'City':user['address']['city']
             }
            )
   
else:
    print("Bad request: ",response.status_code)
    


    

    