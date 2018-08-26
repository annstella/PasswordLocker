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
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
