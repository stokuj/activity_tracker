from django.urls import path
from . import views
from .views import ChangePasswordView

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('register/',views.register, name='register'),

    path('create_post/',views.create_post, name='create_post'),
    path('create_activity/',views.create_activity, name='create_activity'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('post_page/<str:pk>', views.post_page, name='post_page'),

    path('account_settings/', views.account_settings, name='account_settings'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('show_report/', views.show_report, name='show_report'),
    path('show_report2/', views.show_report2, name='show_report2'),
    path('excel/',views.save_csv,name="downloadexcel"),
    path('excel2/',views.delete_post_as_admin, name="downloadexcel2"),
    path('excel3/',views.delete_comment_as_admin, name="downloadexcel3"),
    path('upload/',views.upload, name="upload"),

]