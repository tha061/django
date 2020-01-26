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
import json
import mimetypes


jsonClass = APKAnalysis()
jsonClass.VTsha1 = "Test"
print(jsonClass.name)
print(jsonClass.VTsha256)
print(jsonClass.VTsha1)
print(jsonClass.__dict__)


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

def detail(request):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'uploads/detail.html', {'link': link})


def download_file(request):
    # fill these variables with real values
    fl_path = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder\json.txt'
    filename = 'json.txt'
    fl = open(fl_path, 'r')
    print(fl)
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

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
            APKfilesize = file_size(apkCode +'.apk')
            instance.fileSize = APKfilesize
            instance.firstChar = returnZ(instance.link_text)
            k  = vt_scan(apkCode)
            print(k)
            instance.VT_permallink = k[0]
            instance.VT_sha1 = k[1]
            instance.VT_resource = k[2]
            instance.VT_response = k[3]
            instance.VT_scanId  = k[4]
            instance.VT_msg  = k[5]
            instance.VT_sha256 = k[6]
            instance.VT_md5 = k[7]
            jsonClass.name = apkCode
            jsonClass.fileSize = APKfilesize
            jsonClass.VTpermalink = k[0]
            jsonClass.VTsha1 = k[1]
            jsonClass.VTresource = k[2]
            jsonClass.VTresponsecode = k[3]
            jsonClass.VTscanID  = k[4]
            jsonClass.VTmsg  = k[5]
            jsonClass.VTsha256 = k[6]
            jsonClass.VTmd5 = k[7]

            serialJSON = jsonClass.__dict__
            print(serialJSON)

            jsonFile = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder\json.txt", "w")
            json.dump(serialJSON, jsonFile, indent = 2)

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
