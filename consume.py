'''
This is a file to request data from websites using the 'requests' module in python

We can use this to do get requests from the website we just created and print the 
data in JSON format in the VS terminal 
'''

import requests

response = requests.get('http://127.0.0.1:8000/mysite')
print(response.json())