from django.urls import path
from . import views



app_name = 'uploads'
urlpatterns = [

    path('', views.uploadHere, name='uploadHere'),

    path('download/', views.download, name='download'),

    path('results/<str:appID>', views.results, name='results'),
    path('results/', views.results, name='results'),
    path('<int:link_id>/vote/', views.vote, name='vote'),

    path('test/', views.download_JSONfile, name = 'download_JSONfile'),
    path('certDownload/', views.download_Certfile, name = 'download_Certfile'),
    path('VirusTotalDownload/', views.download_VirusTotal, name = 'download_VirusTotal'),
    path('PrivacyPolicyTextDownload/', views.download_PrivacyPolicyText, name = 'download_PrivacyPolicyText'),
    path('emulator/', views.emulator, name='emulator'),
    path('ERROR/', views.ERROR, name='ERROR'),
]
