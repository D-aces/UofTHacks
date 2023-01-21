from typing import Any, List, Optional
from firebase import firebase

# Connection to Firebase database
firebase = firebase.FirebaseApplication(
    'https://test-fb7e3-default-rtdb.firebaseio.com/')


# Creating a person class

class Person:
    # Attributes of the Person
    name: str
    spouse: str
    children: List[str]
    siblings: List[str]
    mother: str
    father: str

    # Initialization
    def __init__(self, name: str, spouse: str, children: List[str],
                 siblings: List[str],
                 mother: str, father: str) -> None:
        self.name = name
        self.spouse = spouse
        self.children = children
        self.siblings = siblings
        self.mother = mother
        self.father = father

## Method to post to the Firebase Database
# p = Person("Mike Smith", "", [], [], "Susan Smith", "John Smith")
# data = {
#     'Name': p.name,
#     'Mom': p.mother,
#     'Dad': p.father
# }
# post_result = firebase.post('https://test-fb7e3-default-rtdb.firebaseio.com
# /Family', data) print(post_result)

## Method to get data from the Firebase Database
# get_result = firebase.get('/Family/-NMINl9E110r_XZUqVSk', 'Mom')
from typing import Any, List, Optional
from firebase import firebase

# Connection to Firebase database
firebase = firebase.FirebaseApplication(
    'https://test-fb7e3-default-rtdb.firebaseio.com/')


# Creating a person class

class Person:
    # Attributes of the Person
    name: str
    spouse: str
    children: List[str]
    siblings: List[str]
    mother: str
    father: str

    # Initialization
    def __init__(self, name: str, spouse: str, children: List[str],
                 siblings: List[str],
                 mother: str, father: str) -> None:
        self.name = name
        self.spouse = spouse
        self.children = children
        self.siblings = siblings
        self.mother = mother
        self.father = father

## Method to post to the Firebase Database
# p = Person("Mike Smith", "", [], [], "Susan Smith", "John Smith")
# data = {
#     'Name': p.name,
#     'Mom': p.mother,
#     'Dad': p.father
# }
# post_result = firebase.post('https://test-fb7e3-default-rtdb.firebaseio.com
# /Family', data) print(post_result)

# Method to get data from the Firebase Database
get_result = firebase.get('/Family/-NMINl9E110r_XZUqVSk', 'Mom')
print(get_result)

