from typing import Any, List, Optional
from firebase import firebase

# Connection to Firebase database
firebase = firebase.FirebaseApplication(
    'https://test-fb7e3-default-rtdb.firebaseio.com/')


class Person:
    pass

class Person:
    """ Create a person"""
    # Attributes of the Person
    first_name: str
    last_name: str
    spouse: Person
    children: List[Person]
    siblings: List[Person]
    mother: Person
    father: Person

    # Initialization
    def __init__(self, firstname: str, lastname: str) -> None:
        self.first_name = firstname
        self.last_name = lastname
        self.spouse = None
        self.children = []
        self.siblings = []
        self.mother = None
        self.father = None

    def set_parents(self, mom: Optional[Any], dad: Optional[Any]) -> None:
        self.mother = mom
        self.father = dad

    def set_siblings(self, sib:Person) -> None:
        self.siblings.append(sib)

    def set_children(self, child: Person) -> None:
        self.children.append(child)

    def set_spouse(self, spouse: Person) -> None:
        self.spouse = spouse

    def get_name(self) -> str:
        return self.first_name + ' ' + self.last_name


def create_person(firstname: str, lastname: str, spouse: Person,
                  children: List[Person],
                  siblings: List[Person], mother: Person, father: Person) -> dict:
    """ Create a person using the parameters corresponding their firstname,
    lastname, spouse, children, siblings, mother, father and return a dictionary
    version of the person with the attributes as keys."""

    p = Person(firstname, lastname, spouse, children, siblings, mother, father)
    data = {
        "Firstname": p.first_name,
        "Lastname": p.last_name,
        "Spouse": p.spouse,
        "Children": p.children,
        "Siblings": p.siblings,
        "Mother": p.mother,
        "Father": p.father
    }
    return data


def post_result(data: dict) -> str:
    """ Post person unto the database and return string whether it was
    successful.
    """
    try:
        firebase.post(
            'https://test-fb7e3-default-rtdb.firebaseio.com/Family',
            data)
        return "Success"
    except:
        return "Failure"


def get_result() -> dict:
    """ Get family tree from the Firebase Database"""
    return firebase.get('https://test-fb7e3-default-rtdb.firebaseio.com/Family',
                        '')


if __name__ == '__main__':
    mom = Person("Mina", "Runners")
    dad = Person("David", "Runners")
    sis = Person("Julia", "Runners")
    mom.set_siblings(sis)
    mom.set_spouse(dad)
    print(mom.siblings[0].get_name())

