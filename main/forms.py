from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Activity, MyCsv, Comment
import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, )
    first_name = forms.RegexField(
        min_length=4,
        max_length=12,
        regex=r'^([a-zA-Z]+?)([-\s\'][a-zA-Z]+)*?$',
        error_messages={'invalid': ("Wrong first name format!")}
    )
    last_name = forms.RegexField(
        min_length=4,
        max_length=12,
        regex=r'^([a-zA-Z]+?)([-\s\'][a-zA-Z]+)*?$',
        error_messages={'invalid': ("Wrong last name format!")}
    )

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data

    class META:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name']


class PostForm(forms.ModelForm):
    text = forms.RegexField(
        min_length=4,
        max_length=500,
        regex=r'^(?=.{1,500}$)[\w\s]{1,40}(?:[\s]+[\w\s]{1,40}){0,12}$',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        error_messages={'invalid': ("Max number of characters: 500. Max number of charcters for each world: 40")}
    )
    
    class Meta:
        model = Post
        fields = ["text"]


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["activity_name", "activity_category", "activity_duration"]


class ProfileForm(forms.ModelForm):
    profileimg = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))
    userText = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    isPrivate = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ['userText', 'profileimg', 'isPrivate']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.RegexField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        min_length=4,
        max_length=12,
        regex=r'^([a-zA-Z]+?)([-\s\'][a-zA-Z]+)*?$',
        error_messages={'invalid': ("Wrong first name format!")}
    )
    last_name = forms.RegexField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        min_length=4,
        max_length=12,
        regex=r'^([a-zA-Z]+?)([-\s\'][a-zA-Z]+)*?$',
        error_messages={'invalid': ("Wrong last name format!")}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CommentForm(forms.ModelForm):
    text = forms.RegexField(
        min_length=4,
        max_length=100,
        regex=r'^(?=.{1,100}$)[\w\s]{1,30}(?:[\s]+[\w\s]{1,30}){0,2}$',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        error_messages={'invalid': ("Max number of characters: 100. Max number of charcters for each world: 30")}
    )
    
    class Meta:
        model = Comment
        fields = ["text"]

class CsvForm(forms.ModelForm):
    file_name = forms.FileField(max_length=100, validators=[
                                validate_file_extension])

    class Meta:
        model = MyCsv
        fields = ('file_name',)
