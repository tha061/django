from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Link
from . import forms
from .functions import *
#from .searching_mobile_apps_ids0 import *
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
import re
#from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

#from apkutils import


jsonClass = APKAnalysis()

def emulator(request):
    monkeyCMD()
    device = "reee"
    return render(request, 'uploads/emulator.html', {'appID': device} )


    '''
    a  = os.popen("adb devices").readlines()
    device = ""
    time.sleep(5)
    try:
        device = a[1]
    except:
        device = "No device attached"


        os.system("from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice")
        os.system("device = MonkeyRunner.waitForConnection()")

        print("Opening Emulator")
        openEmulator()
        print("emulator Opened")

        a  = os.popen("adb devices").readlines()
        device = ""
        time.sleep(5)
        try:
            device = a[1]
        except:
            device = "No device attached"

        print("install app")
        installApp("com.daystrom.fbattery")

        print("Monkey")
        monkeyCMD()
    '''

def index(request):

    latest_link_list = Link.objects.order_by('-pub_date')[:5]
    context = {'latest_link_list': latest_link_list}
    return render(request, 'uploads/index.html', context)

def detail(request):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'uploads/detail.html', {'link': link})

def download_VirusTotal(request):
    val = request.POST.get('appCode', False);
    appID = val+"VirusTotal.txt"

    fl_path = os.path.join(r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\VirusTotal', appID)
    filename = appID
    fl = open(fl_path, 'r')


    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_JSONfile(request):
    val = request.POST.get('appCode', False);
    appID = val+"JSONFile.txt"

    fl_path = os.path.join(r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder', appID)
    filename = 'json.txt'
    fl = open(fl_path, 'r')


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


def results(request, handle="Didn't work"):

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
            certificatePath = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\original\META-INF\CERT.RSA"%apkCode


            try:
                os.remove(apkPATH)
            except:
                print("nothing to remove")




            os.chdir(apkFolder)
            download_apk(instance.link_text)
            if checkApkDownloaded(instance.link_text):
                print("Doing VT Scan - It will be a minute!")
                k  = vt_scan(apkCode)
                decompileAPK(apkCode, apkFolder, apkFolderCD)  #decompiles APK using apktool
                #apkToZip(apkFolder, apkCode) #This does not work as the manifestfile is not decompiled when converted to ZIP

                if(os.path.exists(manifestPath)):
                    theseUsesPermissions = usesPermissionsFromXML(manifestPath) #collects permissions
                    thesePermissions = permissionsFromXML(manifestPath) #collections permissions
                    serviceList = servicesFromXML(manifestPath) #collects service permissions
                else:
                    theseUsesPermissions = "Can't decompile properly"
                    thesePermissions ="Can't decompile properly"
                    serviceList = "Can't decompile properly"

                try:
                    metaInformation = metaFromWebsite(apkCode) #collects meta-Info
                except:
                    print("Can't connect to android website")
                    metaInformation = "Can't connect to android website"






                smaliDirectory = returnSmaliKey(returnSmaliTuplDict(), getLibrariesDirectories(apkCode))
                smaliFiles = getLibrariesSmali(apkCode)
                APKfilesize = file_size(apkPATH)
                instance.fileSize = APKfilesize
                instance.firstChar = returnZ(instance.link_text)
                instance.VT_permallink = k[0]
                instance.VT_sha1 = k[1]
                instance.VT_resource = k[2]
                instance.VT_response = k[3]
                instance.VT_scanId  = k[4]
                instance.VT_msg  = k[5]
                instance.VT_sha256 = k[6]
                instance.VT_md5 = k[7]
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
                jsonClass.VTtotal = k[8]
                jsonClass.VTpositives = k[9]
                jsonClass.permissions = thesePermissions
                jsonClass.usesPermissions = theseUsesPermissions
                jsonClass.service = serviceList
                jsonClass.metaData = metaInformation[0]
                jsonClass.rating = metaInformation[1]
                jsonClass.description = metaInformation[2]
                jsonClass.links = metaInformation[3]
                jsonClass.smali_Directories = smaliDirectory
                serialJSON = jsonClass.__dict__


                jsonPath = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder", apkCode+"JSONFile.txt")
                jsonFile = open(jsonPath, "w")
                json.dump(serialJSON, jsonFile, indent = 2)
                instance.save()
                print("FORM IS VALID")
                if(os.path.exists(manifestPath)):
                    makeCertificateFile(apkCode)
                else:
                    print("NO CERT FILE")

                dictionary = {'appID':apkCode, 'linkID':handle}
                return render(request,'uploads/detail.html', dictionary)
    else:
            form = forms.CreateLink()
    return render(request, 'uploads/detail.html', {'form':form} )

def vote(request, link_id):
    return HttpResponse("You're voting on link %s." % link_id)

@login_required(login_url="/account/login")
def uploadHere(request):
    form = forms.CreateLink()
    #makeCertificateFile('au.com.hydro.rottnest')
    #PemCertificate('menloseweight.loseweightappformen.weightlossformen')
    #VerifyCertificate('menloseweight.loseweightappformen.weightlossformen')
    #getSmaliFolders('com.chess')
    #print(returnSmaliKey(returnSmaliTuplDict(), getLibrariesDirectories('com.chess')))
    #URL = "https://www.virustotal.com/gui/file/fb7c7fbc4c314efabb1d11676668dcfb7478b4536b5966d3eba15ecbb70cdeea/detection"
    #virusTotalVerdict(URL)
    #print(VTVerdict("menloseweight.loseweightappformen.weightlossformen"))
    #print(getSha("com.yogavpn"))
    #print(vt_scan("com.yogavpn"))
    #print(RSAtoPEM("com.daystrom.fbattery"))
    #manifestPath1  = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\menloseweight.loseweightappformen.weightlossformen\AndroidManifest.xml"
    #print(ReceiversFromXML(manifestPath1))
    #manifestPath2  = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\com.lesmillsondemand\AndroidManifest.xml"
    #print(ReceiversFromXML(manifestPath2))
    #print(getSha('apkpure'))
    #extractAPK('com.softpauer.f1timingapp2014.basic')
    makeCertificateFile('com.disney.disneyplus')



    return render(request, 'uploads/uploads.html', {'form':form})
