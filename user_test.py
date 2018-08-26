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

def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"Annstella")
    self.assertEqual(self.new_user.last_name,"Kagai")
    self.assertEqual(self.new_user.email,"annstellawangui12@gmail.com")
    self.assertEqual(self.new_user.password,"annstella")


if __name__ == '__main__':
    unittest.main()
