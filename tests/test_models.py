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
from django.contrib.auth.models import User 
from main.models import Post, Comment, Activity, Profile

from django.core.files.uploadedfile import SimpleUploadedFile

class PostDef:
    created_at = models.DateTimeField(auto_now_add=True)
    text01    = "description"
    text02   = "tags"

class BasePostModel(TestCase,PostDef):
    
    @classmethod
    def setUpClass(cls):
        super(BasePostModel, cls).setUpClass()
        cls.user = User(username = 'UserForsTestingPosts', email = 'UserForsTestingPosts@email.com', password = 'qJXyNRZPn6Zhh623', first_name = 'firstname',last_name = 'lastname')
        cls.user.save()
        
        cls.post1 = Post(author=cls.user, text=PostDef.text01, created_at = models.DateTimeField(auto_now_add=True))
        cls.post1.save()
        
        cls.post2 = Post(author=cls.user, text=PostDef.text02, created_at = models.DateTimeField(auto_now_add=True))
        cls.post2.save()
        
class CreateSinglePost1Test(BasePostModel, PostDef):
    def test_created_properly(self):
        
        self.assertNotEqual(self.user.username,     '')
        self.assertEqual(self.user.username,        'UserForsTestingPosts')
        self.assertEqual(PostDef.text01,            self.post1.text)
     
class CreateSinglePost2Test(BasePostModel, PostDef):
    def test_created_properly(self):
        
        self.assertNotEqual(self.user.username,     '')
        self.assertEqual(self.user.username,        'UserForsTestingPosts')
        self.assertEqual(PostDef.text02,            self.post2.text)

class BaseCommentModel(TestCase):
        
    @classmethod
    def setUpClass(cls):
        super(BaseCommentModel, cls).setUpClass()
        cls.user = User(username = 'UserForTestingComments', email = 'UserForTestingComments@email.com', password = 'qJXyNRZPn6Zhh623', first_name = 'firstname',last_name = 'lastname')
        cls.user.save()
        
        cls.post = Post(author=cls.user, text="Text of post", created_at = models.DateTimeField(auto_now_add=True))
        cls.post.save()
        
        cls.comment = Comment(post = cls.post, author = cls.user ,text = 'Text of comment', created_at = models.DateTimeField(auto_now_add=True))
        cls.comment.save()
        
class CommentModelTest(BaseCommentModel):
    def test_created_properly(self):
        
        self.assertEqual(self.user.username,        'UserForTestingComments')
        self.assertEqual(self.comment.post,         self.post)
        self.assertEqual(self.comment.author,       self.user)
        self.assertEqual(self.comment.text,         'Text of comment')
        
class BasepProfileModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(BasepProfileModel, cls).setUpClass()
        cls.user = User(username = 'UserForTestingProfile', email = 'UserForTestingProfile@email.com', password = 'qJXyNRZPn6Zhh623', first_name = 'firstname',last_name = 'lastname')
        cls.user.save()
        
        cls.image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        cls.profile = Profile(user=cls.user, userText = 'biography', profileimg = cls.image, isPrivate = True ) #...
        cls.profile.save()
        
class ProfileModelTest(BasepProfileModel):
    def test_created_properly(self):
        
        self.assertEqual(self.user.username,        'UserForTestingProfile')
        self.assertEqual(self.profile.user,         self.user)
        self.assertEqual(self.profile.userText,    'biography')
        self.assertIsNotNone(Profile.isPrivate)
        self.assertIsNotNone(Profile.profileimg)
        
class BaseActivityModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(BaseActivityModel, cls).setUpClass()
        cls.user = User(username = 'UserForsTestingActivities', email = 'UserForsTestingActivities@email.com', password = 'qJXyNRZPn6Zhh623', first_name = 'firstname',last_name = 'lastname')
        cls.user.save()
        
        cls.activity1 = Activity(activity_name="TestActivity1", author=cls.user, activity_category='Swimming', created_at = models.DateTimeField(auto_now_add=True))
        cls.activity1.save()
        cls.activity2 = Activity(activity_name="TestActivity2", author=cls.user, activity_category='', created_at = models.DateTimeField(auto_now_add=True))
        cls.activity2.save()
        
class CreateSingleActivityTest(BaseActivityModel):
    def test_created_properly1(self):
        
        self.assertNotEqual(self.user.username,     '')
        self.assertEqual(self.user.username,        'UserForsTestingActivities')
        self.assertEqual(self.activity1.activity_name,   'TestActivity1')
        self.assertEqual(self.activity1.activity_category,   'Swimming')
        
    def test_created_properly2(self):
        
        self.assertNotEqual(self.user.username,     '')
        self.assertEqual(self.user.username,        'UserForsTestingActivities')
        self.assertEqual(self.activity2.activity_name,   'TestActivity2')
        self.assertNotEqual(self.activity2.activity_category,   'Swimming')