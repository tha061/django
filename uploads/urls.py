from django.urls import path
from . import views



app_name = 'uploads'
urlpatterns = [

    path('', views.uploadHere, name='uploadHere'),
    path('list/', views.upload_list, name='upload_list'),
    path('getFile/', views.getFile, name='getFile'),

    path('download/', views.download, name='download'),

    path('results/<str:appID>', views.results, name='results'),
    path('results/', views.results, name='results'),
    path('<int:link_id>/vote/', views.vote, name='vote'),

    path('uploadsManyAPK', views.uploadsManyAPK, name='uploadsManyAPK'),

    path('test/', views.download_JSONfile, name = 'download_JSONfile'),
    path('certDownload/', views.download_Certfile, name = 'download_Certfile'),
    path('VirusTotalDownload/', views.download_VirusTotal, name = 'download_VirusTotal'),
    path('PrivacyPolicyTextDownload/', views.download_PrivacyPolicyText, name = 'download_PrivacyPolicyText'),
    path('URLRequestsDownload/', views.download_URLRequests, name = 'download_URLRequests'),
    path('SuspiciousURLRequestsDownload/', views.download_SuspiciousURLRequests, name = 'download_SuspiciousURLRequests'),
    path('emulator/', views.emulator, name='emulator'),
    path('avd', views.avd, name='avd'),
    path('avd_results', views.avd_results, name='avd_results'),
    path('ERROR/', views.ERROR, name='ERROR'),
]
