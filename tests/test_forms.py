from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files import File
from django.conf import settings
from django.db import models
from django import setup


import sys
sys.path.append("C:/Users/dv6/Documents/GitHub/PracaInzActivity/Imp/ActivityTracker/activityTracker/")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'activityTracker.settings')

setup()

from django.contrib.auth.models import User #has to be after setup()
from main.models import Post, Comment, Followers, Profile

from django.core.files.uploadedfile import SimpleUploadedFile


### Number of users already in database
users = get_user_model().objects.all()
number_of_users_in_db = users.count()

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_true_is_true(self):
        print("Method: test_true_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

class CreateSingleUserTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testRegister'
        self.email = 'testRegister@email.com'
        self.password = 'qJXyNRZPn6Zhh623'
        self.first_name = 'firstname'
        self.last_name = 'lastname'

    def test_main(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name

        })
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+1)
        
class EmptyPasswordTest(TestCase):
    def setUp(self) -> None:
        self.username = '0testuser2'
        self.email = 'testuser@email.com'
        self.password = ''
        self.first_name = 'firstname'
        self.last_name = 'lastname'


    def test_main(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db)

class EmptyEmailTest(TestCase):
    def setUp(self) -> None:
        self.username = '0testuser2'
        self.email = ''
        self.password = 'qJXyNRZPn6Zhh623'
        self.first_name = 'firstname'
        self.last_name = 'lastname'


    def test_main(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db)
               
class CreateTwoAccountsTest(TestCase):
    def setUp(self) -> None:
        #1st
        self.username = 'testuser1001'
        self.email = 'testuser1001@email.com'
        self.password = 'qJXyNRZPn6Zhh623'
        
        #2nd
        self.username2 = 'testuser10022'
        self.email2 = 'testuser1002@email.com'
        self.password2 = 'qJXyNRZPn6Zhh6232'
    
        self.first_name = 'firstname'
        self.last_name = 'lastname'


    def test_main(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/register/', data={
            'username': self.username2,
            'email': self.email2,
            'password1': self.password2,
            'password2': self.password2,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+2)
        
class CreateTwoIdenticalAccountsTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser1110'
        self.email = 'testusertestuser1110@email.com'
        self.password = 'qJXyNRZPn6Zhh623'
        self.first_name = 'firstname'
        self.last_name = 'lastname'


    def test_main(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+1)
        
class CreateUserWithEmailAsPasswordTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser1111'
        self.email = 'testuser1111@email.com'
        self.password = 'testuser1111@email.com'
        self.first_name = 'firstname'
        self.last_name = 'lastname'


    def test_main(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+0)
        
class CreateUserWithWrongFirstNameTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser1112'
        self.email = 'testuser1112@email.com'
        self.password = 'qJXyNRZPn6Zhh623'
        self.first_name1 = 'firstname01'
        self.first_name2 = 'tomek😔 ÆÆ'
        self.last_name = 'lastname'


    def test_numeric_first_name(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name1,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+0)
        
    def test_weird_characters_first_name(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name2,
            'last_name': self.last_name
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+0)
        
class CreateUserWithWrongLastNameTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser1115'
        self.email = 'testuser1115@email.com'
        self.password = 'qJXyNRZPn6Zhh623'
        self.first_name = 'firstname'
        self.last_name1 = 'lastname02'
        self.last_name2 = 'lastname ½©'

    def test_numeric_last_name(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name1
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+0)
        
    def test_weird_characters_last_name(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name2
        })
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), number_of_users_in_db+0)
           

