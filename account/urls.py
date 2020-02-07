from django.urls import path

from account import views

app_name = 'account'
urlpatterns = [
    path('signup', views.view_signup, name='view_signup'),
    path('login', views.view_login, name='view_login'),
    path('logout', views.view_logout, name='view_logout'),
    path('', views.view_home, name='view_home'),
]
