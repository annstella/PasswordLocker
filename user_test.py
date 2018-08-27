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

def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into the user user_list
    '''
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)

if __name == '__main__':
    unittest.main()

def  test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save multiple user objects to our user_list
    '''
    self.new_user.save_user()
    test_user = User("Test","contact","test@contact.com","abcdefgh")
    test_user.save_user()
    
