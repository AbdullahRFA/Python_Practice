# This Python script is performing the following tasks:
import os
import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Define the file path
directory = '/Users/abdullahnazmus-sakib/Desktop/Code_Practice_A_N_S_383/Python_Practice/JSON_CVS_FILE/'
file_path = os.path.join(directory, 'users_info.csv')

# Ensure the directory exists; if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

if response.status_code == 200:
    data = response.json()
    try:
        print("Current working directory:", os.getcwd())
        
        # Attempt to open and write to the file at the specified path
        with open(file_path, 'w', newline='') as users:
            fieldnames = ['Name', 'E-mail', 'City', 'ZipCode', 'Phone']
            writer = csv.DictWriter(users, fieldnames=fieldnames)
            writer.writeheader()
            
            for user in data:
                writer.writerow(
                    {
                        'Name': user['name'],
                        'E-mail': user['email'],
                        'City': user['address']['city'],
                        'ZipCode': user['address']['zipcode'],
                        'Phone': user['phone']
                    }
                )
        print("File created successfully at:", file_path)
    except Exception as e:
        print("An error occurred while writing the file:", e)
else:
    print("Bad request:", response.status_code)