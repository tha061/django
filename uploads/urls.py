from django.urls import path

from . import views

app_name = "uploads"

urlpatterns = [

    path('', views.uploadHere, name='uploadHere'),

    path('<int:link_id>/', views.detail, name='detail'),

    path('results/', views.results, name='results'),

    path('<int:link_id>/vote/', views.vote, name='vote'),
]
