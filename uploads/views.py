from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Link
from . import forms
from .functions import *
from .searching_mobile_apps_ids0 import *
from .playStore import *
from .download_apk import *
#from googleplay_api.googleplay import GooglePlayAPI
from .trackinglibraries import *

print("KKKKKk")
#print(file_size(r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\menloseweight.loseweightappformen.weightlossformen.apk'))
#k = vt_scan('walking.weightloss.walk.tracker')


#get_app_metainfo('menloseweight.loseweightappformen.weightlossformen.apk')

#download_apk('menloseweight.loseweightappformen.weightlossformen', '1.0.8', r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\APKdump')
#print(app)
# Create your views here.
def index(request):
    latest_link_list = Link.objects.order_by('-pub_date')[:5]
    context = {'latest_link_list': latest_link_list}
    return render(request, 'uploads/index.html', context)

def detail(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'uploads/detail.html', {'link': link})

def results(request):

    if request.method == 'POST':

        form = forms.CreateLink(request.POST, request.FILES)

        if form.is_valid():

            instance = form.save(commit=False)

            apkCode = instance.link_text


            instance.author = request.user
            download_apk(instance.link_text)
            print(apkCode +'.apk')
            print(file_size(apkCode +'.apk'))
            instance.fileSize = file_size(apkCode +'.apk')
            instance.firstChar = returnZ(instance.link_text)

            k  = vt_scan(apkCode)


            instance.VT_permallink = k[0]
            instance.VT_sha1 = k[1]
            instance.VT_resource = k[2]
            instance.VT_response = k[3]
            instance.VT_scanId  = k[4]
            instance.VT_msg  = k[5]
            instance.VT_sha256 = k[6]
            instance.VT_md5 = k[7]

            #instance.fileSize = file_size(r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\'+instance.link_text)
            instance.save()
            print("FORM IS VALID")
            return redirect('uploads:results')
    else:
        form = forms.CreateLink()
    return render(request, 'uploads/detail.html', {'form':form} )

def vote(request, link_id):
    return HttpResponse("You're voting on link %s." % link_id)

def uploadHere(request):
    form = forms.CreateLink()
    return render(request, 'uploads/uploads.html', {'form':form})
