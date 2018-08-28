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
