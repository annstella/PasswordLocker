import unittest
from user import user

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unttest.TestCase: TestCase class that helps in creating test cases
        '''

def setUp(self):
    '''
    set up method to run before each test cases.
    '''
    self.new_user = User("Annstella","Kagai","annstellawangui12@gmail.com","annstella")
