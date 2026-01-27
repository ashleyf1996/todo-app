import pytest

def test_equal(): 
    assert 3 == 3

def test_is_instanse():
    assert isinstance("is a string", str)



def test_boolean():
    validated = True 
    assert validated is True 


def test_type(): 
    assert type('Hello' is str)
    assert type('World' is not int)


def test_greater(): 
    assert 4 < 10 


def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False, False]
    assert 1 in num_list
    assert False in any_list
    assert all(num_list)


class Student: 
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.firstname = first_name
        self.lastname = last_name
        self.major = major
        self.years = years


@pytest.fixture
def default_employee(): 
    return Student('jon', 'doe', 'df', 3)

def test_person_init(default_employee):
    assert default_employee.firstname == 'jon'


