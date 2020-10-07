from mysite import views
from django.contrib import admin
from django.urls import include, path
from database import views


app_name = 'database'
urlpatterns = [
    path('', views.databaseHome, name='databaseHome'),
    path('health-list', views.collectHealthList, name='collectHealthList'),
    path('corpus-csv', views.corpusCSV, name='corpusCSV'),
    path('split-csv', views.splitCSV, name='splitCSV'),
    path('makeURLArray', views.makeURLArray, name='makeURLArray'),
    path('makePPString', views.makePPString, name='makePPString'),
    path('testFunction', views.testFunction, name='testFunction'),

]
