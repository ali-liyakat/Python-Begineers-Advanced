class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

daval = User(10, "Ali", "25 years")
print(daval.name)
print(daval.age)


from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    age: int
    address: Optional[str] = None


# daval = User(id=10, name="Ali", age="25 years")     # error message type error
daval = User(id=10, name="Ali", age=25, address="Lane 600") 
# daval = User(id=10, name="Ali")                      # error message missing error
print(daval.name)
print(daval.age)
print(daval.address)
