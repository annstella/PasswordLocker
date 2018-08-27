import unittest
from user import user

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unttest.TestCase: TestCase class that helps in creating test cases
        '''


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"Annstella")
    self.assertEqual(self.new_user.last_name,"Kagai")
    self.assertEqual(self.new_user.email,"annstellawangui12@gmail.com")
    self.assertEqual(self.new_user.password,"annstella")


def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into the user user_list
    '''
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)




def  test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save multiple user objects to our user_list
    '''
    self.new_user.save_user()
    test_user = User("Test","contact","test@contact.com","abcdefgh")
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)


def test_delete_user(self):

    '''
    test_delete_user to test if we can remove a user from our user list
    '''
    self.new_user.save_user(
    test_user = User("Test","contact","test@contact.com","abcdefgh")
    test_user.save_user()

    self.new_user.delete_user()
    self.assertEqual(len(Contact.contact_list),1)

def test_user_exists(self):
    '''
    test to check if we can return a Boolean if we cannot find the user.
    '''
    self.new_user.save_user()
    test_user = User("Test","contact","test@user.com","abcdefgh")
    test_user.save_user()
    user_exits = User.user_exist("Annstella")

    self.assertTrue(user_exists)

def test_display_all_users(self):
    '''
    method that returns a list of all users saved
    '''

    self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__':
    unittest.main()
