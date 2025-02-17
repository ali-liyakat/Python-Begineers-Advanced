import json

json_string = '''
{
    "name": "Ali",
    "age": 36,
    "is_employ": true,
    "skills": ["Python", "Data Analysis", "ML"],
    "addresses": {
        "street": "36 main street",
        "city": "Keelung"
    }
}
'''

print(type(json_string))

record = json.loads(json_string)        # converted string to dictionary
print(record)

print(type(record))

print(record['name'])


data = {
    "name": "Ali",
    "age": 36,
    "is_employ": False,
    "skills": ["Python", "Data Analysis", "ML"],
    "addresses": {
        "street": "36 main street",
        "city": "Keelung"
    }
}

data_str = json.dumps(data)     # convert dictionary to json string
print(data_str)

print(type(data_str))

# writing json object to file

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

with open("products.json", "r") as f:
    products = json.load(f)
print(products)

print(type(products))

print(products[0])
print(products[0]['price'])


json_string = '''
{
    "books": [
        {"title": "The Magic Of Thinking Big", "author": "David J. Schwartz", "published": 1959},
        {"title": "Chanakya Neeti", "author": "B.K. Chaturvedi", "published": 2009},
        {"title": "How to Win Friends and Influence People", "author": "Dale Karnegie", "published": 1936}
    ],
    "status_code": 200
}
'''

data = json.loads(json_string)
print(data)

books = data['books'] 
print(books)

book_list = [{'title': book['title'], 'author': book['author']} for book in books]
print(book_list)


# Malformed jSON strings

json_string = '''
{
    "name": "Arun",
    "age": 30
    "employees": true
}
'''

try:
    json.loads(json_string)
except json.JSONDecodeError as e:
    print(f" failed to decode, {e}")