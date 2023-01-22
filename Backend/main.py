from typing import Any, List, Optional
from firebase import firebase

# Connection to Firebase database
firebase = firebase.FirebaseApplication(
    'https://test-fb7e3-default-rtdb.firebaseio.com/')


# To keep track
class Person:
    pass


class Person:
    """ Create a person"""
    # Attributes of the Person
    first_name: str
    last_name: str
    id: str
    spouse: str
    children: str
    siblings: str
    mother: str
    father: str

    # Initialization
    def __init__(self, firstname: str, lastname: str) -> None:
        self.first_name = firstname
        self.last_name = lastname
        self.id = ""
        self.spouse = ""
        self.children = ""
        self.siblings = ""
        self.mother = ""
        self.father = ""

    def get_name(self) -> str:
        return self.first_name + ' ' + self.last_name

    def set_id(self, id: str) -> None:
        self.id = id

    def set_siblings(self, siblings: str) -> None:
        self.siblings = siblings

    def set_mother(self, mom: str) -> None:
        self.mother = mom

    def set_father(self, dad: str) -> None:
        self.father = dad

    def set_spouse(self, spouse: str) -> None:
        self.spouse = spouse


def create_data_form(p: Person) -> dict:
    """ Create a person using the parameters corresponding their firstname,
    lastname, spouse, children, siblings, mother, father and return a dictionary
    version of the person with the attributes as keys."""
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


## These methods are for more complicated version of family tree
# def add_siblings_db(id: str, sib: dict) -> dict:
#     """ Add siblings to the database according to the id """
#     firebase.post(
#         'https://test-fb7e3-default-rtdb.firebaseio.com/Family' + '/' + id + '/Siblings',
#         sib)
#
#
# def add_spouse_db(id: str, spouse: dict) -> dict:
#     """ Add spouse to the database according to the id """
#     firebase.post(
#         'https://test-fb7e3-default-rtdb.firebaseio.com/Family' + '/' + id + '/Spouse',
#         spouse)
#
#
# def add_mom_db(id: str, mom: dict) -> dict:
#     """ Add mom to the database according to the id """
#     firebase.post(
#         'https://test-fb7e3-default-rtdb.firebaseio.com/Family' + '/' + id + '/Mother',
#         mom)
#
#
# def add_dad_db(id: str, dad: dict) -> dict:
#     """ Add dad to the database according to the id """
#     count += 1
#     firebase.post(
#         'https://test-fb7e3-default-rtdb.firebaseio.com/Family' + '/' + id + '/Father',
#         dad)
#
#
# def add_children_db(id: str, child: dict) -> dict:
#     """ Add child to the database according to the id """
#     firebase.post(
#         'https://test-fb7e3-default-rtdb.firebaseio.com/Family' + '/' + id + '/Children',
#         child)


def post_result(p: Person, data: dict) -> None:
    """ Post person unto the database and return string of id
    """
    res = firebase.post('https://test-fb7e3-default-rtdb.firebaseio.com/Family',
                        data)
    print(res['name'])
    p.set_id(res['name'])


def get_result() -> dict:
    """ Get family tree from the Firebase Database"""
    return firebase.get('https://test-fb7e3-default-rtdb.firebaseio.com/Family',
                        '')


if __name__ == '__main__':
    # More complicated version of family tree
    # me = Person("Tiana", "King")
    # kid = Person("Tamara", "King")
    # kid2 = Person("Tia", "King")
    # husband = Person("Jeff", "King")
    #
    # # Converting the people into dictionary
    # d1 = create_data_form(me)
    # d2 = create_data_form(kid)
    # d4 = create_data_form(kid2)
    # d3 = create_data_form(husband)
    #
    # # Inputting them into database
    # post_result(me, d1)
    # add_spouse_db(me.id, d3)
    # add_children_db(me.id, d2)
    # add_children_db(me.id, d4)

    # Simple immediate family tree
    p = Person("Bill", "Gates")
    p.set_siblings("William Gates")
    p.set_father("Charles Gates")
    p.set_mother("Joan Gates")
    p.set_spouse("Sandra Gates")

    # Create the data format to submit to database
    data = create_data_form(p)
    post_result(p, data)

    # Retrieve data from database
    res = get_result()

    # Print out the family
    for i in res[p.id]:
        print(i + ':' + res[p.id][i])
