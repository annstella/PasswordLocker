import unittest
# import pyperclip
from user import User , Credent

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unttest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_user = User ("Annstella","Kagai","annstellawangui12@gmail.com","annstella") #create user object

    def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """
        User.user_list = []

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
        self.new_user.save_user()
        test_user = User("Test","contact","test@contact.com","abcdefgh")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Test","contact","test@user.com","abcdefgh")
        test_user.save_user()
        user_exists = User.user_exist("Annstella")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)


class TestCredent(unittest.TestCase):
    """
    Test class that defines test cases for the credent class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_credent = Credent ("Annstella","kuitwo","ann12k") #create user object

    def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """
        Credent.credent_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credent.user_name,"kuitwo")

    def test_save_credent(self):
        """
        test to check if the credent object is saved on credent list
        """
        self.new_credent.save_credent() #save user
        self.assertEqual(len(Credent.credent_list),1)

    def test_save_multiple_credent(self):
        """
        To check if we can save multiple objects into list
        """
        self.new_credent.save_credent()
        test_credent = Credent ("instagram","clanzym","nutella")
        test_credent.save_credent()
        self.assertEqual(len(Credent.credent_list),2)

    def test_delete_credent(self):
            '''
            test_delete_credent to test if we can remove credent from our credent list
            '''
            self.new_credent.save_credent()
            test_credent = Credent ("instagram","clanzym","nutella") # new credential
            test_credent.save_credent()

            self.new_credent.delete_credent()# Deleting a credential object
            self.assertEqual(len(Credent.credent_list),1)

    def test_find_credent_by_user_name(self):
        '''
        test to check if we can find a credent by user name and display information
        '''

        self.new_credent.save_credent()
        test_credent = Credent ("instagram","clanzym","nutella") # new credential
        test_credent.save_credent()

        found_credent = Credent.find_by_user_name("clanzym")

        self.assertEqual(found_credent.pswrd,test_credent.pswrd)

    def test_credent_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credent.save_credent()
        test_credent = Credent ("instagram","clanzym","nutella") # new credential
        test_credent.save_credent()

        credent_exists = Credent.credent_exist("clanzym")

        self.assertTrue(credent_exists)

    def test_display_all_credent(self):
        '''
        method that returns a list of all credent saved
        '''

        self.assertEqual(Credent.display_credent(),Credent.credent_list)

if __name__ == '__main__':
    unittest.main()
