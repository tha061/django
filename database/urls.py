from mysite import views
from django.contrib import admin
from django.urls import include, path
from database import views


app_name = 'database'
urlpatterns = [
    path('', views.databaseHome, name='databaseHome'),

]
