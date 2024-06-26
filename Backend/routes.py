import re
import random
import base64
import numpy as np
from datetime import date
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from  sqlalchemy.exc import OperationalError
from flask import Blueprint, redirect, url_for
from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash


from .base import db
from .user_class import User
from .assessment_class import Assessment

# from .functions import load_img, transform, load_model, predict, convert_to_obj



main = Blueprint('main', __name__)


email = ''



# Route to get the username and password in the login screen
@main.route('/', methods = ['POST'])
def intro():
    # Move to login screen
    response = {'response': 'Log In page'}
    print('Hello there, I am Nour Your Companion')
    return jsonify(response)






# Route to get the username and password in the login screen (Done)
@main.route('/login', methods = ['POST'])
def login_info():

    global email

    response = {}
   # Get the data from the Json dictionary
    email = request.form.get('email')
    password = request.form.get('password')

    # Convert email to lowercase
    email = email.lower()

    print('Log In Route,' , f'email: {email}', f'Password: {password}')

    user = User.query.filter_by(email=email).first()

    #print(type(user.id))
    #print(user.email)
    #print(user.username)
    #print("User's Password:", user.password)
    #hashed_password = generate_password_hash(password, method='pbkdf2')
    #print('Entered Password:', hashed_password)
    #print(check_password_hash(user.password, hashed_password))

    # User Doesn't exist
    if not user:
        print("Login Failed, Email doesn't exist", f'Entered Email: {email}', f'Entered Password: {password}')
        # Send a JSON response back to the client
        response = {'response': 'Access Denied'}
        return jsonify(response)        # Login failed
    # Check if the entered password and the stored password matches
    if (not check_password_hash(user.password, password)):
        print('Login Failed, Wrong Password', f'Entered Email: {email}', f'Entered Password: {password}')
        # Send a JSON response back to the client
        response = {'response': 'Access Denied'}
        return jsonify(response)        # Login failed
    # Log In was Successful
    else:
        print('Success, 'f'Email: {email}', f'Password: {password}')
        # Send a JSON response back to the client
        response = {'response': 'Access Allowed', 'user_id': str(user.id)}
        return jsonify(response)
    







# A route for the sign up screen (Done)
@main.route('/signup', methods = ['POST'])
def signup_info():

    global email

    response = {}
    regex_1 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    regex_2 = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    data = request.form
    username = data.get('username').strip()
    email = data.get('email').strip()
    password = data.get('password').strip()
    age = data.get('age').strip()
    gender = data.get('gender').strip()
    if gender=='Female':
        gender='F'
    else:
        gender='M'


    # Convert email to lowercase
    email = email.lower()

    # Password Validation
    capital = any(char.isupper() for char in password)
    small = any(char.islower() for char in password)
    special_character = bool(regex_2.search(password))
    email_val, pass_val = 0, 0

    # Check the password for small, capital & special characters
    if capital and small and special_character:
        pass_val = 1    # Set flag to true
    # Check the email format
    if(re.fullmatch(regex_1, email)):
        email_val = 1   # Set flag to true

    print('Sign Up Information, 'f'Username: {username}', f'Email: {email}', f'Password: {password}')
    print(f'Email: {bool(re.fullmatch(regex_1, email))}')
    print(f'Capital: {capital}')
    print(f'Small: {small}')
    print(f'Special Character: {special_character}')

    # Both, Email & Password don't match the criteria
    if (not pass_val) and (not email_val):
        print('Sign Up Failed Due to Password & Email')
        response = {'response': 'Failed Password and Email'}
        return jsonify(response)
    # Password doesn't match the criteria
    if not pass_val:
        print('Sign Up Failed Due to Password')
        print(f'Failed Password: {password}')
        response = {'response': 'Failed Password'}
        return jsonify(response)
    # Email doesn't match the criteria
    if not email_val:
        print('Sign Up Failed Due to Email')
        response = {'response': 'Failed Email'}
        return jsonify(response)
    # Email & Password accepted
    else:
        print('Signed Up Successfully, 'f'Username: {username}', f'Email: {email}', f'Password: {password}')
        hashed_password = generate_password_hash(password, method='pbkdf2')
        print('Hashed Password is: ', hashed_password)

        # Check if the email already exists
        if User.query.filter_by(email=email).first():
            print('Sign Up Failed Due to Duplicate Email')
            response = {'response': 'Failed: Email already exists'}
            return jsonify(response)
        # Email doesn't exist
        else:
            # add info from form to user
            new_user = User(
            username = f'{username}', 
            password = hashed_password,
            email = email,
            gender = gender, #'None'
            age = age,
            )
            
            try:
                db.session.add(new_user)
                db.session.commit()
                print('user id: ', new_user.id) # Get user ID
                response = {'response': 'Signup successful'}
            except OperationalError:
                print('Operational Error Encountered')
            except IntegrityError:
                db.session.rollback()   # Rollback the transaction
                print('Integrity Error: User with this email already exists')
                response = {'response': 'Email already exists'}
            except Exception as e:
                db.session.rollback()
                print(f'Error during signup: {str(e)}')
                response = {'response': 'Internal Server Error'}
            return jsonify(response)




# A route for the sign up screen (Done)
@main.route('/quiz', methods = ['POST'])
def quiz():

    global email

    response = {}
    score = int(request.form.get('score'))         # Get the Computed Score For each question
    user = User.query.filter_by(email=email).first()

    print('Quiz Route,' , f'Obtained Score For User: {email}')
    print(f'Score: {score}')
    
    try:
        user_id = user.id
        username = user.username

        # add new score to the database
        new_user = Assessment(
        username = username, 
        fk_user_id = user_id,
        email = email,
        score = int(request.form.get('score')), #score
        )

        db.session.add(new_user)
        db.session.commit()
        print('user id: ', user_id) # Get user ID
        response = {'message': 'Signup successful'}
    except OperationalError:
        print('Operational Error Encountered')
    except Exception as e:
        db.session.rollback()
        print(f'Error during obtaining quiz score: {str(e)}')
        response = {'message': 'Internal Server Error'}
    return jsonify(response)

    
    
