from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User._meta.get_field('email')._unique = True
# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.author.id, filename)


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate(value):
    too_small = timedelta(minutes=5)
    if value < too_small:
        raise ValidationError(
            _('%(value)s Minimum time is 5 minutes'),
            params={'value': value},
        )
    too_big = timedelta(hours=12)
    if value > too_big:
        raise ValidationError(
            _('%(value)s Maximum time is 12hours'),
            params={'value': value},
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userText = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='default_profile_image.jpg', blank=True)
    isPrivate = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user.username


class Followers(models.Model):
    followee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_followee_created')
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_follower_created')

    def __str__(self):
        return self.user


class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    activity_category = (
        ('Swimming', ('Swimming')),
        ('Yoga', ('Yoga')),
        ('Running', ('Running')),
        ('Snowboarding', ('Snowboarding')),
        ('Push-ups', ('Push-ups')),
        ('Walking', ('Walking')),
        ('Surfing', ('Surfing')),
        ('Diving', ('Diving')),
        ('Cycling', ('Cycling')),
        ('Climbing Stairs', ('Climbing Stairs')),
    )

    # […]
    activity_category = models.CharField(
        max_length=32,
        choices=activity_category,
        default='available',
    )
    activity_duration = models.DurationField(
        default=timedelta, validators=[validate])

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity_name


class Post(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post


class PostFull():
    def __init__(self, post, comments):
        self.post = post
        self.comments_list = comments


class MyCsv(models.Model):

    file_name = models.FileField(
        upload_to='csvs/', max_length=100, validators=[validate_file_extension])
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
