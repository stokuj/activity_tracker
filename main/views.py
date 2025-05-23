from typing import List
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from .models import Post, Profile, Followers, Comment, PostFull, Activity, MyCsv
from .forms import RegisterForm, PostForm, ProfileForm, ActivityForm, UpdateUserForm, CsvForm, CommentForm
from itertools import chain
import os
import random
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
import humanfriendly
from django.http import HttpResponse
import csv
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pandas as pd
import plotly.express as px
import csv
from csv import reader

###########################################################################################
# Loggin not nedded
###########################################################################################


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return create(form, request)
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})

# created with refacting used in register


def create(form, request):
    password = form.cleaned_data.get('password1')
    username = form.cleaned_data.get('username')
    last_name = form.cleaned_data.get('last_name')
    email = form.cleaned_data.get('email')
    first_name = form.cleaned_data.get('first_name')

    newUser = User(username=username, last_name=last_name,
                   first_name=first_name, email=email)
    newUser.set_password(password)
    newUser.save()
    new_profile = Profile.objects.create(user=newUser)
    new_profile.save()
    login(request, newUser, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('/update_profile')


def home(request):
    feed = []
    user_following = Followers.objects.filter(follower=request.user.id)

    user_following_list = [users.followee for users in user_following]
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(author=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))
    feed_list.sort(key=lambda x: x.created_at, reverse=False)

    full_post_list = []
    comments_list = []
    for post in feed_list:
        comments_set = Comment.objects.filter(post=post).order_by('created_at')
        comments_list.append(comments_set)
        comments_list_final = list(chain(*comments_list))
        comments_list_final.sort(key=lambda x: x.created_at, reverse=False)
        full_post_list.append(PostFull(post, comments_list_final[-4:]))
        comments_list.clear()

    # creating the suggestions list
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.followee)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(
        all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(
        new_suggestions_list) if (x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile_list = []

    username_profile = [users.id for users in final_suggestions_list]
    for ids in username_profile:
        profile_lists = Profile.objects.filter(user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    if post_id := request.POST.get("post-id2"):
        if request.method == "POST":
            post = Post.objects.filter(id=post_id).first()
            post.delete()
            return redirect(reverse('/search/'))

    return render(request, 'main/home.html', {"posts": full_post_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})



def search(request):
    username_profile = []
    username_profile_list = []

    if request.method == 'POST':
        search_val = request.POST['search_val']
        username_object = User.objects.filter(username__icontains=search_val)

        username_profile.extend(users.id for users in username_object)
        for ids in username_profile:
            profile_lists = Profile.objects.filter(user=ids)
            username_profile_list.append(profile_lists)

        username_profile_list = list(chain(*username_profile_list))

    return render(request, 'main/search.html', {'username_profile_list': username_profile_list})


def profile(request, pk):
    user_obj = User.objects.get(username=pk)

    try:
        user_profile = Profile.objects.get(user=user_obj)
    except Exception:
        new_profile = Profile.objects.create(user=user_obj)
        new_profile.save()
        user_profile = Profile.objects.get(user=user_obj)

    try:
        avatar_path = user_profile.profileimg.path
        if not os.path.isfile(avatar_path):
            print("Avatar file not found!")
            user_profile.profileimg = "default_profile_image.jpg"
            user_profile.save()
            
    except Exception as e:
        print(f'Error: {e}')

    posts = Post.objects.filter(author_id=user_obj.id)
    posts.order_by('created_at')

    full_post_list = []
    comments_list = []
    for post in posts:
        comments_set = Comment.objects.filter(
            post=post).order_by('-created_at')
        comments_list.append(comments_set)
        comments_list_final = list(chain(*comments_list))
        comments_list_final.sort(key=lambda x: x.created_at, reverse=False)
        full_post_list.append(PostFull(post, comments_list_final[-4:]))
        comments_list.clear()
    follower = request.user
    user = pk

    if Followers.objects.filter(follower=follower.id, followee=user_obj).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
    user_followers = len(Followers.objects.filter(followee=user_obj))
    user_following = len(Followers.objects.filter(follower=user_obj))
    context = {
        'user_obj': user_obj,
        'user_profile': user_profile,
        'posts': full_post_list,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }

    if request.method == "POST":
        if post_id := request.POST.get("post-id"):
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user):
                post.delete()
                return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'main/profile.html', context)


def post_page(request, pk):
    post_obj = Post.objects.get(id=pk)
    user = request.user
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.post = post_obj
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()


    if request.method == 'POST' and 'comment_id' in request.POST:
        if comment_id := request.POST.get("comment_id"):
            comment = Comment.objects.filter(id=comment_id).first()
            if comment and (comment.author == user):
                comment.delete()
                return redirect(request.META.get('HTTP_REFERER'))

    comments_list = Comment.objects.filter(post=post_obj)

    context = {
        'post_obj': post_obj,
        'comments_list': comments_list,
        'form': form,
    }

    return render(request, 'main/post_page.html', context)

def contact(request):
    return render(request, 'main/contact.html', {})
###########################################################################################
# Login Nedded
###########################################################################################



@login_required(login_url="/login")
def delete_post_as_admin(request):
    if post_id := request.POST.get("post-id"):
        post = Post.objects.filter(id=post_id).first()
        post.delete()
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, "main/home.html", {})


@login_required(login_url="/login")
def delete_comment_as_admin(request):
    if request.method == 'POST' and 'comment_id_admin' in request.POST:
        if comment_id := request.POST.get("comment_id_admin"):
            comment = Comment.objects.filter(id=comment_id).first()
            comment.delete()
            return redirect(request.META.get('HTTP_REFERER'))

        return render(request, "main/home.html", {})


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('/profile/' + request.user.username)
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


@login_required(login_url="/login")
def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.author = request.user
            activity.save()
            return redirect("/create_activity/")
    else:
        form = ActivityForm()

    if request.method == "POST":
        if activity_id := request.POST.get("activity-id"):
            activity = Activity.objects.filter(id=activity_id).first()
            if activity and (activity.author == request.user):
                # path = os.curdir + post.image.url
                # os.remove(path)
                activity.delete()
                return redirect("/create_activity/")

    if request.method == "POST":
        if activity_id := request.POST.get("activity-post"):
            activity = Activity.objects.filter(id=activity_id).first()
            if activity and (activity.author == request.user):

                form = PostForm()
                post = form.save(commit=False)
                delta = activity.activity_duration
                # text = request.POST['Textarea1']
                # print(text)
                post.text = "I was " + activity.activity_category + \
                    " for " + humanfriendly.format_timespan(delta)
                post.author = request.user
                post.save()

                return redirect(reverse('home'))

    user_obj = User.objects.get(username=request.user)
    list_of_activities = Activity.objects.filter(author_id=user_obj.id)
    list_of_activities.order_by('created_at')

    return render(request, 'main/create_activity.html', {"form": form, "list_of_activities": list_of_activities})


@login_required(login_url="/login")
def save_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="data.csv"'},
    )
    user_obj = User.objects.get(username=request.user)
    list_of_activities = Activity.objects.filter(author_id=user_obj.id)
    list_of_activities.order_by('created_at')

    writer = csv.writer(response)
    # writer.writerow(['activity_name', 'activity_category', 'author_id', 'created_at', 'activity_duration'])

    for x in list_of_activities:
        writer.writerow([x.pk, x.activity_name, x.activity_category,
                        x.author.pk, x.created_at, x.activity_duration])

    return response




@login_required(login_url="/login")
def follow(request):

    if request.method != 'POST':
        return redirect('/')
    follower = User.objects.get(username=request.POST['follower'])
    user_profile = request.POST['user_prof']
    user_object = User.objects.get(username=user_profile)
    if tempFoll := Followers.objects.filter(
        follower=follower, followee=user_object
    ).first():
        delete_follower = Followers.objects.get(
            follower=follower, followee=user_object)
        delete_follower.delete()
    else:
        new_follower = Followers.objects.create(
            follower=follower, followee=user_object)
        new_follower.save()
    return redirect('profile/'+user_object.username)


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.userText = form.cleaned_data.get('userText')
            profile.profileimg = form.cleaned_data.get('profileimg')
            profile.save()
            return redirect('/home')
    else:
        form = ProfileForm()

    return render(request, 'registration/create_profile.html', {"form": form})


@login_required
def user_settings(request):
    user_obj = request.user
    if request.method == 'POST':
        user_nick = request.POST['nname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        e_mail = request.POST['email']

        user_obj.username = user_nick
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.email = e_mail
        user_obj.save()

        return redirect('/profile/' + request.user.username)
    return render(request, 'main/user_settings.html', {'user_obj': user_obj})


@login_required
def prof_change(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('image') is None:
            image = user_profile.profileimg
            information = request.POST['infox']
            user_profile.profileimg = image
            user_profile.userText = information

            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            information = request.POST['info']
            user_profile.profileimg = image
            user_profile.userText = information

            user_profile.save()

        return redirect('/profile/' + request.user.username)
    return render(request, 'main/prof_change.html', {'user_profile': user_profile})


@login_required
def change_pass(request):
    user_obj = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_pass')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    context = {'user_obj': user_obj, }

    return render(request, 'main/change_pass.html', {'form': form, })


@login_required
def account_settings(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            print("ttttttttttttttl")
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='/')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'main/account_settings.html', {'user_form': user_form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        # user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        # if user_form.is_valid() and profile_form.is_valid():
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='home')
    else:
        # user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'main/update_profile.html', {'profile_form': profile_form})


@login_required(login_url="/login")
def show_report(request):

    user_obj = User.objects.get(username=request.user)
    list_of_categories = ['Swimming', 'Yoga', 'Running', 'Snowboarding',
                          'Push-ups', 'Walking', 'Surfing', 'Diving', 'Cycling', 'Climbing Stairs']
    cat_dur = [0,      0,         0,              0,          0,
               0,         0,        0,         0,                 0]

    for x in range(10):
        list_of_activities = Activity.objects.filter(
            author_id=user_obj.id, activity_category=list_of_categories[x])

        for i in list_of_activities:
            delta = i.activity_duration
            # days to sec to mins
            cat_dur[x] += round(((delta.days * 24 * 60 *
                                60) + delta.seconds)/60)

    #
    df = pd.DataFrame({
        'Activity Categories': ['Swimming',    'Yoga',    'Running',  'Snowboarding',    'Push-ups',  'Walking',  'Surfing',   'Diving',  'Cycling', 'Climbing Stairs'],
        'Time in minutes': [cat_dur[0], cat_dur[1],   cat_dur[2],      cat_dur[3],    cat_dur[4], cat_dur[5], cat_dur[6], cat_dur[7], cat_dur[8],        cat_dur[9]]
    })

    # df.loc[df['Time in minutes'] < 10, 'Activity Categories'] = 'Other Activities' # Represent only large countries
    fig = px.bar(df, x='Activity Categories',
                 y='Time in minutes', color='Activity Categories')

    # df.loc[df['Time in minutes'] < 10, 'Activity Categories'] = 'Other countries' # Represent only large countries
    # fig = px.pie(df, names='Activity Categories', values='Time in minutes', color='Activity Categories')
    plot_div = plot(fig, output_type='div')
    #

    list_of_activities = Activity.objects.filter(author_id=user_obj.id)
    return render(request, 'main/show_report.html', context={'plot_div': plot_div, "list_of_activities": list_of_activities})


@login_required(login_url="/login")
def show_report2(request):
    try:
        user_obj = User.objects.get(username=request.user)
        list_of_categories = ['Swimming', 'Yoga', 'Running', 'Snowboarding',
                            'Push-ups', 'Walking', 'Surfing', 'Diving', 'Cycling', 'Climbing Stairs']
        cat_dur = [0,      0,         0,              0,          0,
                0,         0,        0,         0,                 0]

        for x in range(10):
            list_of_activities = Activity.objects.filter(
                author_id=user_obj.id, activity_category=list_of_categories[x])

            for i in list_of_activities:
                delta = i.activity_duration
                # days to sec to mins
                cat_dur[x] += round(((delta.days * 24 * 60 *
                                    60) + delta.seconds)/60)

        #
        df = pd.DataFrame({
            'Activity Categories': ['Swimming',    'Yoga',    'Running',  'Snowboarding',    'Push-ups',  'Walking',  'Surfing',   'Diving',  'Cycling', 'Climbing Stairs'],
            'Time in minutes': [cat_dur[0], cat_dur[1],   cat_dur[2],      cat_dur[3],    cat_dur[4], cat_dur[5], cat_dur[6], cat_dur[7], cat_dur[8],        cat_dur[9]]
        })

        # Represent only large countries
        df.loc[df['Time in minutes'] < 30,
            'Activity Categories'] = 'Other Activities'
        fig = px.pie(df, names='Activity Categories',
                    values='Time in minutes', color='Activity Categories')
        plot_div = plot(fig, output_type='div')
        #

        list_of_activities = Activity.objects.filter(author_id=user_obj.id)
        return render(request, 'main/show_report2.html', context={'plot_div': plot_div, "list_of_activities": list_of_activities})
    except Exception:
        print("Exception")

@login_required(login_url="/login")
def upload(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    # check whether it's valid:
    if form.is_valid():
        form.save()
        form = CsvForm()
        obj = MyCsv.objects.get(activated=False)
        user_obj = User.objects.get(username=request.user)

        Activity.objects.filter(author_id=user_obj.id).delete()
        with open(obj.file_name.path, 'r') as read_obj:
            csv_reader = reader(read_obj)
            try:
                for row in csv_reader:

                    thisUser = User.objects.get(id=row[3])
                    activity = Activity(pk=row[0], activity_name=row[1], activity_category=row[2],
                                        author=thisUser, created_at=row[4], activity_duration=row[5])
                    activity.save()
            except Exception:
                print("An exception occurred")
                MyCsv.objects.all().delete()

        obj.activated = True
        obj.save()
        if os.path.isfile(obj.file_name.path):
            os.remove(obj.file_name.path)

        MyCsv.objects.all().delete()

    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect("/create_activity/")
    else:
        form = CsvForm()

    context = {'form': form, }
    return render(request, 'main/upload.html', context)


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'main/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
