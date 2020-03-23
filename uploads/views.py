from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Link
from . import forms
from .functions import *
from .searching_mobile_apps_ids0 import *
from .playStore import *
from .download_apk import *
from .adbFunctions import *
#from googleplay_api.googleplay import GooglePlayAPI
from .trackinglibraries import *
import json
import mimetypes
import shutil
import subprocess
from .apk import *
from .apk_decompiler import *
from os import chdir, system
from django.contrib.auth.decorators import login_required
import sys
from io import BytesIO
from .certificate_Functions import *
from OpenSSL import SSL
import time
#from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

#from apkutils import


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

def emulator(request):
    openEmulator()

    a  = os.popen("adb devices").readlines()
    device = ""
    time.sleep(5)
    try:
        device = a[1]
    except:
        device = "No device attached"

    print("Monkey")
    monkeyCMD()


    print("install app")
    installApp()


    #device = MonkeyRunner.waitForConnection()
    #print(device)

    return render(request, 'uploads/emulator.html', {'appID': device} )

def index(request):
    latest_link_list = Link.objects.order_by('-pub_date')[:5]
    context = {'latest_link_list': latest_link_list}
    return render(request, 'uploads/index.html', context)

def detail(request):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'uploads/detail.html', {'link': link})


def download_JSONfile(request):
    val = request.POST.get('appCode', False);
    appID = val+"JSONFile.txt"

    fl_path = os.path.join(r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder', appID)
    filename = 'json.txt'
    fl = open(fl_path, 'r')
    #print(fl)
    print("ARE WE HERE")
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_Certfile(request):

    val = request.POST.get('appCode', False);
    appID = val+"CertFile.txt"
    fl_path = os.path.join(r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\certificate', appID)
    filename = appID

    fl = open(fl_path, 'r')
    #print(fl)
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def results(request):
    #apkClass = APK(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\com.daystrom.fbattery.apk")
    if request.method == 'POST':
        form = forms.CreateLink(request.POST, request.FILES)
        if form.is_valid():

            instance = form.save(commit=False)
            apkCode = instance.link_text
            instance.author = request.user

            apkPATHold = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite", apkCode+".apk")
            apkPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", apkCode+".apk")
            zipPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", apkCode+".zip")
            apkFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads"
            apkFolderCD = r"Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownload"
            manifestPath  = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\AndroidManifest.xml"%apkCode

           #    print(permissionsFromXML(manifestPath))

            try:
                os.remove(apkPATH)
            except:
                print("nothing to remove")

            os.chdir(apkFolder)
            download_apk(instance.link_text)

            print("apkPathold: "+apkPATHold)
            print("apk FOLDER: "+apkFolder)

            #shutil.move(apkPATHold, apkFolder) #this needs to be fixed, fifx it so the APK is downloaded to the correct folder straight away
            #shutil.copy(apkPATH, zipPATH)
            #getManifest(zipPATH)
            print("NNNNNNNNNNNNNNNNNOOOOOOOOOOOOOOOOO")
            os.chdir(apkFolder)

            os.system("cd "+apkFolderCD)
            os.system("apktool d "+apkCode+".apk ./"+apkCode+".apk")
            time.sleep(10)
            print("Sleep done")


            theseUsesPermissions = usesPermissionsFromXML(manifestPath)
            thesePermissions = permissionsFromXML(manifestPath)
            metaInformation = metaFromWebsite(apkCode)
            serviceList = servicesFromXML(manifestPath)



            print(file_size(apkPATH))
            APKfilesize = file_size(apkPATH)

            instance.fileSize = APKfilesize
            instance.firstChar = returnZ(instance.link_text)
            print("here")
            k  = vt_scan(apkCode)
            print("VT Scan is here")
            print(k)

            smaliDirectory = getLibrariesDirectories(apkCode)
            smaliFiles = getLibrariesSmali(apkCode)

            instance.VT_permallink = k[0]
            instance.VT_sha1 = k[1]
            instance.VT_resource = k[2]
            instance.VT_response = k[3]
            instance.VT_scanId  = k[4]
            instance.VT_msg  = k[5]
            instance.VT_sha256 = k[6]
            instance.VT_md5 = k[7]
            #jsonClass.permissions = thesePermissions
            #jsonClass.usesPermissions = theseUsesPermissions
            instance.metaData = metaInformation[0]
            instance.rating = metaInformation[1]
            instance.description = metaInformation[2]

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
            jsonClass.permissions = thesePermissions
            jsonClass.usesPermissions = theseUsesPermissions
            jsonClass.service = serviceList
            jsonClass.metaData = metaInformation[0]
            jsonClass.rating = metaInformation[1]
            jsonClass.description = metaInformation[2]
            jsonClass.smali_Directories = smaliDirectory
            jsonClass.smali_Files = smaliFiles


            serialJSON = jsonClass.__dict__
            #print(serialJSON)

            jsonPath = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder", apkCode+"JSONFile.txt")
            jsonFile = open(jsonPath, "w")
            json.dump(serialJSON, jsonFile, indent = 2)
            instance.save()
            print("FORM IS VALID")
            makeCertificateFile(apkCode)


            dictionary = {'appID':apkCode}
            #return redirect('uploads:results')
            return render(request,'uploads/detail.html', dictionary)
    else:
        form = forms.CreateLink()
    return render(request, 'uploads/detail.html', {'form':form} )

def vote(request, link_id):
    return HttpResponse("You're voting on link %s." % link_id)

@login_required(login_url="/account/login")
def uploadHere(request):
    #metaFromWebsite()
    form = forms.CreateLink()
    apkCode = "menloseweight.loseweightappformen.weightlossformen"

    #manifestPath  = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\AndroidManifest.xml"%apkCode
    #print(usesLibraryFromXML(manifestPath))
    return render(request, 'uploads/uploads.html', {'form':form})
