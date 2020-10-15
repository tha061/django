from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Link
from . import forms
from django.core.files import File
from .functions import *
from .playStore import *
from .download_apk import *
from .adbFunctions import *
from .adb_Functions import *
from .trackinglibraries import *
from .machineLearningFunctions import *
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
#from OpenSSL import SSL
import time
import re
from django.core.files.base import ContentFile
from .filters import *
import html2text
from .models import Document
from .filepaths import *


#This is just a class that contains variables that store information regarding the static and meta-info analysis of an APK
#See the "function.py" file for the class definition


#This is a placeholder View for the running of the emulator
def emulator(request):

    device = "This is a placeholder - Emulator is currently not functioning"

    #Returns the mysite\uploads\templates\uploads\emulator.html file and parses 'device' as an argument
    return render(request, 'uploads/emulator.html', {'appID': device} )


#This simply displays the "download" page
def detail(request):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'uploads/download.html', {'link': link})

#This function will download the VirusTotal JSON results to the users computer
#It is used in mysite\uploads\templates\uploads\download.html on the "VirusTotal" download button
def download_VirusTotal(request):
    #Gets the title of the app that was just analysed from the request

    val = request.POST.get('appCode', False);

    instanceID = request.POST.get('instanceID', False);
    test = request.POST

    obj = Link.objects.get(id=int(instanceID))
    VTFilePath = obj.VTFile.path
    print(VTFilePath)


    #Because VirusTotal results are stored in the format appID + "VirusTotal" as a txt file, appIDVT is the name of the corresponding VirusTotal results file
    appIDVT = val+"VirusTotal.txt"

    #This is the path to the VirusTotal results file
    fl_path = obj.VTFile.path

    #opened file
    fl = open(fl_path, 'r')

    #determines the MIME type of the file
    mime_type, _ = mimetypes.guess_type(fl_path)
    print("MIME:")
    print(mime_type)

    #Returns the file
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % appIDVT
    return response

#This function will download the Static and Meta-info JSON results to the users computer
#It is used in mysite\uploads\templates\uploads\download.html on the "Static and Meta-Info" download button
def download_JSONfile(request):

    val = request.POST.get('appCode', False);
    Sha256 = request.POST.get('Sha256', False);
    #appID is the total file name
    appID = val+"JSONFile.txt"

    instanceID = request.POST.get('instanceID', False);
    obj = Link.objects.get(id=int(instanceID))
    jsonFilePath = obj.jsonFile.path

    #fl_path is the path to the file
    fl_path = jsonFilePath
    filename = 'json.txt'
    fl = open(fl_path, 'r')

    #Returns the correct file and mime_type of the file upon clicking the "download" button
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

#This function will download the Certificate info results to the users computer
#It is used in mysite\uploads\templates\uploads\download.html on the "Static and Meta-Info" download button
def download_Certfile(request):

    val = request.POST.get('appCode', False);
    #appID is the file name of the just analyzed APK
    appID = val+"CertFile.txt"

    instanceID = request.POST.get('instanceID', False);
    obj = Link.objects.get(id=int(instanceID))
    certFilePath = obj.certFile.path

    #path of the certificate file for the relevant APK
    fl_path = certFilePath
    filename = appID

    fl = open(fl_path, 'r')

    #Returns the correct file and mime_type of the file upon clicking the "download" button
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_PrivacyPolicyText(request):

    val = request.POST.get('appCode', False);
    #appID is the file name of the just analyzed APK
    print("val:")
    print(val)
    appID = val+".txt"
    print("appID: "+appID)

    instanceID = request.POST.get('instanceID', False);
    obj = Link.objects.get(id=int(instanceID))


    filename = appID
    policyPATH = returnPolicyPath(val)
    fl = open(policyPATH, 'r')

    #Returns the correct file and mime_type of the file upon clicking the "download" button
    mime_type, _ = mimetypes.guess_type(policyPATH)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_URLRequests(request):
    val = request.POST.get('appCode', False);
    #appID is the file name of the just analyzed APK
    print("val:")
    print(val)
    apkCode = val
    filename = apkCode +"_requested_urls.txt"

    requestedURLSPath = returnURLSRequestedPath(apkCode)
    fl = open(requestedURLSPath, 'r')

    #Returns the correct file and mime_type of the file upon clicking the "download" button
    mime_type, _ = mimetypes.guess_type(requestedURLSPath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_SuspiciousURLRequests(request):
    val = request.POST.get('appCode', False);
    #appID is the file name of the just analyzed APK
    print("val:")
    print(val)
    apkCode = val
    filename = apkCode +"suspicious_requested_urls.txt"

    requestedURLSPath = returnURLSRequestedSharingPath(apkCode)
    fl = open(requestedURLSPath, 'r')

    #Returns the correct file and mime_type of the file upon clicking the "download" button
    mime_type, _ = mimetypes.guess_type(requestedURLSPath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


#Upon submitting an APK for analysis, the "results" function is called.
#This function will conduct all the static, meta-info and run the emulator.
#Currently, it just conducts the static and meta-info collection,
#however, in the future it will use an emulator to conduct dynamic analysis

def staticANDprivacyAnalysis(apkCode, instance, jsonClass):
    apkPATH = returnAPKPath(apkCode)
    zipPATH = returnAPKZIP(apkCode)
    apkFolder = filepaths_APKFolder
    policyPATH = returnPolicyPath(apkCode)
    apkFolderCD = filepaths_returnAPKPathCD
    manifestPath  = returnAPKManifestPath(apkCode)
    requestedURLSPath = returnURLSRequestedPath(apkCode)
    jsonPath = returnAPKJSON(apkCode)
    VirusTotalPath = returnAPKVirusTotal(apkCode)
    CertPath = returnAPKCERT(apkCode)
    mitmdumpsPath = returnAPKMitmdumps(apkCode)

    #print(getTextFromHTML("https://www.bodygrooveondemand.com/privacy")[0])
    #Run VirusTotal Scan, returns results in a list called 'VirusTotalResults'
    print("Doing VT Scan - It will be a minute!")
    VirusTotalResponse = vt_scan(apkCode)
    VirusTotalResults  = VirusTotalResponse.get('list')
    CheckVTLater  = VirusTotalResponse.get('checkVTLater')


    #decompiles APK using apktool, the output is just a folder
    decompileAPK(apkCode, apkFolder, apkFolderCD)

    #If a manifest file can be found in the resulting folder, collect permissions and services from the file
    #Inserts the results in to a list, which will then be displayed in the JSON file
    if(os.path.exists(manifestPath)):
        theseUsesPermissions = usesPermissionsFromXML(manifestPath) #collects permissions
        thesePermissions = permissionsFromXML(manifestPath) #collections permissions
        serviceList = servicesFromXML(manifestPath) #collects service permissions
    else:
        #If the file can't be found, the JSON file will display the below text
        theseUsesPermissions = "Can't decompile properly"
        thesePermissions ="Can't decompile properly"
        serviceList = "Can't decompile properly"


    try:
        #Will try and connect to the Google Play website to scrape the meta-info database
        #Saves the information in the form of a list
        metaInformation = metaFromWebsite(apkCode)
        AndroidWebCantConnect = False
    except Exception as e:
        print("Error in metaFromWebsite()")
        print(e)
        print("Can't connect to android website-------------------")
        metaInformationText = "Can't connect to android website"
        AndroidWebCantConnect = True


    if AndroidWebCantConnect == False:
        privacyPolicyResults = getTextFromHTML(metaInformation[3].get("Privacy Policy"))
    else:
        privacyPolicyResults = ['NA', True]

    try:
        CSVPermissionsResults = usesPermissionsForCSV(manifestPath)
    except:
        CSVPermissionsResults = None


    smaliDirectory = returnSmaliKey(returnSmaliTuplDict(), getLibrariesDirectories(apkCode))

    smaliFiles = getLibrariesSmali(apkCode)


    #Will find the file_size of the APK
    APKfilesize = file_size(apkPATH)
    sha256Calculated = getSha(apkCode)
    instance.link_text = apkCode
    instance.fileSize = APKfilesize
    instance.sha256 = sha256Calculated
    instance.firstChar = returnZ(instance.link_text)

    instance.VT_permallink = VirusTotalResults[0]
    instance.VT_sha1 = VirusTotalResults[1]
    instance.VT_resource = VirusTotalResults[2]
    instance.VT_response = VirusTotalResults[3]
    instance.VT_scanId  = VirusTotalResults[4]
    instance.VT_msg  = VirusTotalResults[5]
    instance.VT_sha256 = VirusTotalResults[6]
    instance.VT_md5 = VirusTotalResults[7]
    if AndroidWebCantConnect == False:
        instance.metaData = metaInformation[0]
        instance.rating = metaInformation[1]
        instance.description = metaInformation[2]
        instance.privacyText = metaInformation[3].get("Privacy Policy")
        instance.smaliList = smaliDirectory.get('library')
        jsonClass.metaData = metaInformation[0]
        jsonClass.rating = metaInformation[1]
        jsonClass.description = metaInformation[2]
        jsonClass.links = metaInformation[3]
        jsonClass.numInstalls = metaInformation[4]
        jsonClass.developer = metaInformation[5]
    else:
        instance.metaData = "NA"
        instance.rating = "NA"
        instance.description ="NA"
        instance.privacyText = "NA"
        instance.smaliList = "NA"
        jsonClass.metaData = "NA"
        jsonClass.rating = "NA"
        jsonClass.description = "NA"
        jsonClass.links ="NA"
        jsonClass.numInstalls = "NA"
        jsonClass.developer = "NA"
        jsonClass.rating = "NA"

    jsonClass.name = apkCode
    jsonClass.fileSize = APKfilesize
    jsonClass.sha256 = sha256Calculated
    jsonClass.VTpermalink = VirusTotalResults[0]
    jsonClass.VTsha1 = VirusTotalResults[1]
    jsonClass.VTresource = VirusTotalResults[2]
    jsonClass.VTresponsecode = VirusTotalResults[3]
    jsonClass.VTscanID  = VirusTotalResults[4]
    jsonClass.VTmsg  = VirusTotalResults[5]
    jsonClass.VTsha256 = VirusTotalResults[6]

    jsonClass.VTmd5 = VirusTotalResults[7]
    jsonClass.VTtotal = VirusTotalResults[8]
    jsonClass.VTpositives = VirusTotalResults[9]
    try:
        jsonClass.VTratio = str(int(jsonClass.VTpositives)/int(jsonClass.VTtotal))
    except:
        jsonClass.VTratio = "error - need to upload file not just hash"
    jsonClass.permissions = thesePermissions
    jsonClass.usesPermissions = theseUsesPermissions
    jsonClass.service = serviceList

    jsonClass.smali_Directories = smaliDirectory.get('library')
    if(AndroidWebCantConnect == False):
        jsonClass.privacyText = metaInformation[3].get("Privacy Policy")
    else:
        jsonClass.privacyText = "Couldn't Connect to Google Play"


    privacyPolicyText = privacyPolicyResults[0]
    jsonClass.PPNoContact =privacyPolicyResults[1]
    if(len(privacyPolicyText) == 0):
        jsonClass.PPEmpty = True
    else:
        jsonClass.PPEmpty = False


    #print("Privacy policy text: -------------------------")
    #print(privacyPolicyText)
    #print("End of policy text: -------------------------")
    if(PPShares3rdParty(privacyPolicyText)):

        PPClaims3rdPartySharing = True
    else:

        PPClaims3rdPartySharing = False

    print("Just finished 3rd party analysis")

    print("PPClaims3rdPartySharing: "+str(PPClaims3rdPartySharing))
    jsonClass.PolicySharesInfo3rdParty = PPClaims3rdPartySharing

    print("Creating Privacy Policy File")
    #print("Privacy policy text............")
    #print(privacyPolicyText)
    #privacyFile = open(policyPATH, "w")




    '''
    try:

        privacyFile.write(privacyPolicyText)

    except Exception as e:
        print("exception: ")
        print(e)
        print("Couldn't get the url for privacy policy")
    privacyFile.close()
    '''



    ####### DYNAMIC ANALYSIS ###########
    monkeyCMD(apkCode, instance)
    mitmdumpDecompile(apkCode, instance)
    networkResults = detectTrackersInHeaders(makeTrackingHeadersArray(),requestedURLSPath, apkCode)
    anyNetworkTraffic = networkResults[2]
    trackingNetworkTraffic = networkResults[3]

    jsonClass.networkTraffic = anyNetworkTraffic
    jsonClass.networkTrafficTracking = trackingNetworkTraffic

    print("Static Contradiction ----")
    jsonClass.libraryContradiction = contradiction((smaliDirectory.get('AnyTrackingLibrary')), jsonClass.PolicySharesInfo3rdParty)

    print("Network Contradiction ----")
    jsonClass.networkTrafficContradiction = contradiction(jsonClass.networkTrafficTracking, jsonClass.PolicySharesInfo3rdParty)


    #update jsonClass if we had to upload APK
    print("----------------CheckVTLater: "+str(CheckVTLater))

    if(CheckVTLater == True):
        print("In CheckVTLater")
        VirusTotalResults = vt_scan_onlyHashLookup(instance.sha256)
        print("VirusTotal Results - a second time ----------")
        print(str(VirusTotalResults))
        updateVirusTotalResults(VirusTotalResults, jsonClass)
        updateVirusTotalResults(VirusTotalResults, instance)
        print("should have updated them")

    resultsList = []
    resultsList.append(apkCode)
    resultsList.append(jsonClass.rating)
    resultsList.append(jsonClass.numInstalls)
    resultsList.append(jsonClass.developer)
    resultsList.append("Health and Fitness")
    resultsList.append(jsonClass.fileSize)
    resultsList.append(jsonClass.VTpermalink)
    resultsList.append(jsonClass.VTtotal)
    resultsList.append(jsonClass.VTpositives)
    resultsList.append(jsonClass.VTratio)
    resultsList.append(CSVPermissionsResults.get("permissionListString"))
    resultsList.append(CSVPermissionsResults.get("dangerous"))
    resultsList.append(CSVPermissionsResults.get("signature"))
    resultsList.append(CSVPermissionsResults.get("normal"))
    resultsList.append(CSVPermissionsResults.get("developerDefined"))
    resultsList.append(listToStringSemiColon(smaliDirectory.get('library')))
    resultsList.append(listToStringSemiColon(smaliDirectory.get('libraryCategory')))

    #print("Targeted ads: "+ str((smaliDirectory.get('TargetedAds')))+" analytics: "+str((smaliDirectory.get('Analytics')))  "+" MobileAnalytics: "+str((smaliDirectory.get('MobileAnalytics'))))
    resultsList.append(str((smaliDirectory.get('TargetedAds'))))
    resultsList.append(str((smaliDirectory.get('Analytics'))))
    resultsList.append(str((smaliDirectory.get('MobileAnalytics'))))
    resultsList.append(str((smaliDirectory.get('AnyTrackingLibrary'))))
    resultsList.append(jsonClass.privacyText)
    resultsList.append(jsonClass.PolicySharesInfo3rdParty)
    resultsList.append(jsonClass.PPNoContact)
    resultsList.append(jsonClass.PPEmpty)
    resultsList.append(jsonClass.networkTraffic)
    resultsList.append(jsonClass.networkTrafficTracking)
    resultsList.append(jsonClass.libraryContradiction)
    resultsList.append(jsonClass.networkTrafficContradiction)

    if jsonClass.libraryContradiction or jsonClass.networkTrafficContradiction:
        jsonClass.contradiction = True

    else:
        jsonClass.contradiction = False

    resultsList.append(jsonClass.contradiction)

    serialJSON = jsonClass.__dict__




    jsonFile = open(jsonPath, "w")
    json.dump(serialJSON, jsonFile, indent = 2)
    jsonFile.close()


    print("FORM IS VALID")

    try:
        makeCertificateFile(apkCode)
    except Exception as e:
        print("Couldn't make certificate file")
        print(e)


    savePrivacyPolicyTextToFile(policyPATH, privacyPolicyText)
    SaveFiletoDatabase(jsonPath, "Static", instance, apkCode)
    SaveFiletoDatabase(VirusTotalPath, "VT", instance, apkCode)
    SaveFiletoDatabase(CertPath, "CertFile", instance, apkCode)

    print(instance.jsonFile)
    print(instance.VTFile)
    print(instance.certFile)

    print("CHECKING ID")
    print(instance.link_text)
    print(instance.id)

    VT_sha256 = instance.VT_sha256

    #check if apk was able to be installed

    if os.path.exists(mitmdumpsPath):
        resultsList.append("True")
    else:
        resultsList.append("False")

    dictionary = {'apkCode':apkCode, 'linkID':"Not working", "Sha256": VT_sha256, "instanceID": instance.id, "results-CSV-List":resultsList}
    print(instance.privacyText)



    return dictionary


def results(request, appID="Wrong"):
    print("CHECKING DYNAMIC")


    #If the request is a POST, then it will begin the analysis,
    #What it "really" checks is whether the user just went to the url "http://127.0.0.1:8000/uploads/results" i.e. a GET request
    #Or is the user being redirected to "http://127.0.0.1:8000/uploads/results" after submitting an APK for analysis i.e. a POST request
    if request.method == 'POST':

        #My Django "Model" is called "Link", a "Model" is a definitive database
        #'forms' refers to the forms.py file, and CreateLink is a class that initializes a new Link model object
        #Essentially form ends up just being the text that is parsed through the App Garadyi 'uploads' webpage i.e. what APK is to be analyzed
        print("request.POST and request.FILES")
        print(request.POST)
        print(request.FILES)
        form = forms.CreateLink(request.POST, request.FILES)
        print("form: ")
        print(form)
        print("type of form: ")
        print(str(type(form)))


        #is_valid() checks if all the variable within 'form' have been declared correctly
        #essentiall, this checks if form's variable 'link_text' contains text
        if form.is_valid():

            #creates an instance of the form
            instance = form.save(commit=False)
            print("instance")
            print(instance)
            print("type of instance: ")
            print(str(type(instance)))


            #This is the text the user parses through the 'uploads' page
            apkCode = instance.link_text

            #This is the users name that is logged in that submitted the analysis request
            instance.author = request.user

            #These are paths to important places within my folderstructure.
            apkPATH = returnAPKPath(apkCode)
            zipPATH = returnAPKZIP(apkCode)
            apkFolder = filepaths_APKFolder
            policyPATH = returnPolicyPath(apkCode)
            apkFolderCD = filepaths_returnAPKPathCD
            manifestPath  = returnAPKManifestPath(apkCode)
            requestedURLSPath = returnURLSRequestedPath(apkCode)


            #If there is an existing .apk file with the same name as the currently analysed APK, then , it will be removed
            try:
                os.remove(apkPATH)
            except:
                print("nothing to remove")


            #Download's the APK to the APK Folder
            os.chdir(apkFolder)
            download_apk(instance.link_text)
            print("Just finishing downloading APK....")
            #If the APK has been succesfully downloaded, continue with analysis
            if checkApkDownloaded(instance.link_text):
                print("Check if APK Downloaded")
                jsonClass = APKAnalysis()
                dictionary = staticANDprivacyAnalysis(apkCode, instance, jsonClass)
                #dictionary = {'apkCode':"this APK", 'linkID':"Not working", "Sha256": "someSHA", "instanceID": 999}
                ####### DYNAMIC ANALYSIS ###########
                #monkeyCMD(apkCode, instance)
                #mitmdumpDecompile(apkCode, instance)
                #detectTrackersInHeaders(makeTrackingHeadersArray(),requestedURLSPath, apkCode)


                return render(request,'uploads/download.html', dictionary)
            print("do we get stuck here????")
    else:
            print("in else")
            form = forms.CreateLink()
            print(form)
            print("APKCODE: ")
            print(appID)
            obj = Link.objects.get(id=int(appID))
            obj_text = obj.link_text
            print("obj text: "+obj_text)
            return render(request, 'uploads/download.html', {'form':form, 'appID':appID, 'apkCode': obj_text, 'instanceID':int(appID)})
    return redirect('uploads:ERROR')

def ERROR(request):
    return render(request, 'uploads/error.html')

def avd(request):
    print(getFirstDevice())

    return render(request, 'uploads/avd.html')

def avd_results(request):
    form = forms.CreateLink()
    instance = form.save(commit=False)
    print("HEEREEE")
    print(instance.link_text)
    test = "com"
    print("REQUEST")
    print(request)
    return render(request, 'uploads/avd_results.html', {'form':form, 'test':test})

def vote(request, link_id):
    return HttpResponse("You're voting on link %s." % link_id)

@login_required(login_url="/account/login")
def uploadHere(request):
    form = forms.CreateLink()
    instance = form.save(commit=False)
    print("HEEREEE")
    print(instance.link_text)
    test = "com"
    print("REQUEST")
    print(request)

    #jsonPath = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder\com.chessJSONFile.txt"
    ##jsonFile = open(jsonPath, "w")
    #instance.jsonFile = File(jsonFile)

    return render(request, 'uploads/uploads.html', {'form':form, 'test':test})

def upload_list(request):

    return render(request, 'uploads/list.html')

def getFile(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('uploads:getFile')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'uploads/list.html', context)

def uploadsManyAPK(request):
    #this views reads a list and performs analysis on every apk in the list and prints info to a csv file
    APKList = filepaths_APKList
    apkFolder = filepaths_APKFolder
    resultsCSV = filepaths_ResultsCSV

    APKlist = makeAPKListArray(APKList)
    print("FILE PATH:")
    print(filepaths_path)

    for item in APKlist:
        os.chdir(apkFolder)
        timeoutBoolean = False
        try:
            download_apk(item)
            #print("Just finishing downloading APK....")
        except FunctionTimedOut:
            print("Could not download with 100 seconds - something wrong with the file")
            print("Download unsuccessful --")
            f = open(resultsCSV, "a", encoding="utf-8")
            f.write("\n"+item+" took too long to download")
            f.close()
            timeoutBoolean = True

        except Exception as e:
            print(e)
            print("Could not download APK....")


        #If the APK has been succesfully downloaded, continue with analysis
        if checkApkDownloaded(item) and timeoutBoolean == False:
            jsonClass = APKAnalysis()

            f = open(resultsCSV, "a", encoding="utf-8")
            form = forms.CreateLink()
            instance = form.save(commit=False)
            #mitmdumpDecompile(item, instance)
            try:
                results = getResultsInList(item, instance, jsonClass).get('results-CSV-List')

                CSVLineResults = listToStringCSV(results)
                print("results: ")
                print(results)
            except Exception as e:
                CSVLineResults = str(e)
                print("Couldn't do this properly for some reason")


            f.write("\n"+CSVLineResults)
            f.close()
        else:
            print("Download unsuccessful --")
            f = open(resultsCSV, "a", encoding="utf-8")
            f.write("\n"+item+" took too long to download")
            f.close()
    #print(list)

    apk_id = APKlist[0]
    print(apk_id)
    return render(request, 'uploads/uploadsManyAPK.html')

def getResultsInList(apkCode, instance, jsonClass):
    return staticANDprivacyAnalysis(apkCode, instance, jsonClass)
    ####### DYNAMIC ANALYSIS ###########
    #monkeyCMD(apkCode, instance)
    #mitmdumpDecompile(apkCode, instance)
    #detectTrackersInHeaders(makeTrackingHeadersArray(),requestedURLSPath, apkCode)
