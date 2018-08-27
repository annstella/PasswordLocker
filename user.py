class User:
    """
    Class that generates new instances of users
    """

    user_list = []


    def __init__(self,first_name,last_name,email,password):
        '''
        __init__method that helps us define properties for our objects

        Args:
            first_name: New user first name.
            last_name : New user last name.
            number: New user phone number.
            email : New user email address.
            password: New user password.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

   def setUp(self):
    '''
    set up method to run before each test cases.
    '''
    self.new_user = User("Annstella","Kagai","annstellawangui12@gmail.com","annstella")

   def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list[]


    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved contact from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def user_exist(cls,first_name):
        '''
        Method that checks if a user exists from the user list.
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return True

   return False

   @classmethod
   def display_users(cls):
       '''
       method that returns the user list
       '''
       return cls.user_list

class Credent:
    '''
    class that generates new instances of the user's credent
    '''
    credent_list = []
    def __init__(self,acc_name,user_name,pswrd):
        self.acc_name = acc-name
        self.user_name = user_name
        self.pswrd = pswrd

    def save_credent(self):
        '''
        save_credent method saves objects into list
        '''
        Credent.credent_list.append(self)

   def delete_credent(self):
       '''
       delete_credent method deletes a saved credent from the credent_list
       '''
       Credent.credential_list.remove(self)
