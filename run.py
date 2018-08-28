#!/usr/bin/env python3.6
from user import User

def create_user(fname,lname,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    contact.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    contact.delete_user()

def find_user(email):
    '''
    Function that finds a user by email and returns the user
    '''
    return User.find_by_email(email)

def check_existing_users(email):
    '''
    Function that check if a user exists with that email and return a Boolean
    '''
    return User.user_exist(email)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


def main():
    print("Hello. What is your name?")
    contact_name = input()
    print(f"Hello {contact_name}. what would you like to do?")
    print('\n')

    while True:

     print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

     short_code = input().lower()


    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Email address ...")
                            e_address = input()

                            print("Set password ...")
                            s_address = input()

                            save_users(create_user(f_name,l_name,e_address,s_password)) # create and save new contact.
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')

    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.email_address}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont have any users saved yet")
                                    print('\n')

    elif short_code == 'fc':

                            print("Enter the email you want to search for")

                            search_email = input()
                            if check_existing_users(search_email):
                                    search_user = find_user(search_email)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That user does not exist")

    # elif short_code == "ex":
    #                         print("Bye .......")
    # break
    # else:
    #     print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()
