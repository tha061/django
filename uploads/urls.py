from django.urls import path

from . import views

app_name = 'uploads'
urlpatterns = [

    path('', views.uploadHere, name='uploadHere'),

    path('detail/', views.detail, name='detail'),

    #path('results/', views.results, name='results'),
    path('results/', views.results, name='results'),

    path('<int:link_id>/vote/', views.vote, name='vote'),

    path('test/', views.download_JSONfile, name = 'download_JSONfile'),
    path('certDownload/', views.download_Certfile, name = 'download_Certfile'),

    path('emulator/', views.emulator, name='emulator'),

]
