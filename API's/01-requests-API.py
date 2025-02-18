import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data[0])
else:
    print("Error: " + response.status_code)



url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "titles": "foo",
    "body": "bar",
    "userId": 1
}

response  = requests.post(url, json=data)
print(response.status_code)

if response.status_code == 201:
    created_post = response.json()
    print(created_post)
else:
    print("failed to create data")



'''
                # ------COMMOM STATUS CODES ----
                200 :- OK
                201 :- CREATED
                400 :- Bad Request
                401 :- Unauthorized
                404 :- Not Found
                500 :- Internal Server Error

'''

# URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Sending a GET request
response = requests.get(url)

# Handling different status codes
if response.status_code == 200:
    print("Request was successful!")
    print(response.json())
elif response.status_code == 404:
    print("Resource not found.")
else:
    print(f"Failed with status code: {response.status_code}")


url = "https://jsonplaceholder.typicode.com/posts"

param = {
    "userId": 1
}

response = requests.get(url, params=param)
print(response.status_code)




# Currency conversion API
app_id = "cef5d2b8ca5f45d0841a1729b3abf92d"

url = "https://openexchangerates.org/api/latest.json?app_id=cef5d2b8ca5f45d0841a1729b3abf92d"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)