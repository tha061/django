from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from uploads.models import Link
from uploads.forms import CreateLink
import pandas as pd
from uploads.filters import LinkFilter
import play_scraper
import re
import os
import csv
from uploads.functions import getTextFromHTML, makeTrackingHeadersArray,detectTrackersInHeaders, getAPKHandlesfromThesisList
from uploads.trackinglibraries import vt_uploadfile
from  uploads.machineLearningFunctions import *

@login_required(login_url="/account/login")
def databaseHome(request):
    print("in database home")
    print(getSet())
    filter = LinkFilter(request.GET, queryset = Link.objects.all())


    test = "normie"
    print("filter: ")
    print(filter)
    queryset = filter.qs
    context = {
        "object_list": queryset,
        "filter":filter,
        "test":test
    }

    return render(request, 'database/database.html', context)

def corpusCSV(request):
    for i in range(1,351):

        TrainingBoolean = True
        ThirdPartyBoolean = False

        PPDirectory = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\COMP4092\Corpus\APP-350_v1.1-1\APP-350_v1.1\annotations"
        filename = "policy_%s.yml"%str(i)
        PPFile = open(os.path.join(PPDirectory, filename), "r+")

        lines = PPFile.readlines()

        if "TEST" in lines[2]:
            TrainingBoolean = False
        allText = ""

        for line in lines:
            allText = allText + line
        ThirdPartyBoolean = check3rdParty(allText, i)

        segment_text_positions = [m.start() for m in re.finditer('segment_text: ', allText)]
        sentence_text_positions = [m.start() for m in re.finditer('sentence_text: ', allText)]

        annotation_positions = [anno.start() for anno in re.finditer('annotations:', allText)]
        text_positions = segment_text_positions+sentence_text_positions
        text_positions.sort()


        entire_text = ""
        for i in range(0,len(text_positions)):
            text = text_positions[i]
            text_end = annotation_positions[i]
            if text in sentence_text_positions:
                entire_text += allText[text+15:text_end-1]
            else:
                entire_text += allText[text+14:text_end-1]

        entire_text_single = entire_text.replace("\n", " ")
        entire_text_single = entire_text_single.replace("\t", " ")
        entire_text_single = entire_text_single.replace("     ", " ")
        entire_text_single = entire_text_single.replace(",", " ")
        entire_text_single = entire_text_single.replace("\"", "")



        #print(entire_text)
        SharingInfo = "negative"
        if(ThirdPartyBoolean == True):
            SharingInfo = "positive"

        corpusCSV = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\6Oct.txt","a")
        #corpusCSV.write(SharingInfo+", "+str(TrainingBoolean)+"\n")
        corpusCSV.write(SharingInfo+", "+entire_text_single+", "+str(TrainingBoolean)+"\n")
        #corpusCSV.write(entire_text_single+"\n")

        corpusCSV.close()
    return render(request, 'database/health-list.html')

@login_required(login_url="/account/login")
def collectHealthList(request):


    markedList = []
    print("in here")
    file = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\thesisList.txt", "a+")#write mode
    file.write("Id," +"\t" + "Category,"+"\t"+"Price"+"\n")
    file.close()
    print("file closed")
    print(list(getSet()))

    recursiveHealthList('com.walgreenshearthealthmobileapp', list(getSet()), markedList)

        #print(x.get("app_id"))
    return render(request, 'database/health-list.html')

def recursiveHealthList(startID, list, markedList):

    file = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\thesisList.txt", "a+")#write mode
    file.write("Id," +"\t" + "Category,"+"\t"+"Price"+"\t"+"Installs"+"\n")
    count = 0

    for x in play_scraper.similar(startID):
        price = play_scraper.details(x.get('app_id')).get('price')
        category = play_scraper.details(x.get('app_id')).get('category')
        installs = play_scraper.details(x.get('app_id')).get('installs')
        if 'HEALTH_AND_FITNESS' in play_scraper.details(x.get('app_id')).get('category') and price == '0':
            if x.get('app_id') not in list:
                file = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\thesisList.txt", "a+")
                file.write(x.get('app_id')+",\t"+ str(category) +",\t"+price+",\t"+installs+"\n")
                count += 1

                file.close()
                list.append(x.get('app_id'))
                print("adding to list")
            else:
                #file = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\thesisList.txt", "a+")

            #    file.write(x.get('app_id')+",\t"+ "already in list \n")
                print("not adding to list")
            #    file.close()
                #file.`write(x.get('app_id')+'\n')


    markedList.append(startID)
    for x in list:
        if x not in markedList:
            recursiveHealthList(x,list,markedList)
            break;



'''
def checkCategory(dict):
    print(dict.get('app_id'))
    return True

def checkPrice(dict):
    print(dict.get('app_id'))
    return True

'''
def checkInstalls(installs):
    value = ''.join(c for c in installs if c.isdigit())
    installNumber = int(value)
    if installNumber > 9999:
        return True
    else:
        return False


def checkCategory(id):
    print(play_scraper.details(id).get('category'))
    if 'HEALTH_AND_FITNESS' in play_scraper.details(id).get('category'):

        return True
    return False


def checkPrice(id):
    print(play_scraper.details(id).get('price'))
    if play_scraper.details(id).get('price') == '0':

        return True
    return False

def getSet():
    existingIDs = set()
    file = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\thesisList.txt", "r")
    readLines = file.readlines()
    for line in readLines:
        string = line.split(",")[0]
        existingIDs.add(string)
        #set.add(string)

    return existingIDs

def check3rdParty(text, i):
    ThirdParyList = [
    'Contact_3rdParty',
    'Contact_City_3rdParty',
    'Contact_E_Mail_Address_3rdParty',
    'Contact_Password_3rdParty',
    'Contact_Phone_Number_3rdParty',
    'Contact_Postal_Address_3rdParty',
    'Contact_ZIP_3rdParty',
    'Demographic_3rdParty',
    'Demographic_Age_3rdParty',
    'Demographic_Gender_3rdParty',
    'Identifier_3rdParty',
    'Identifier_Ad_ID_3rdParty',
    'Identifier_Cookie_or_similar_Tech_3rdParty',
    'Identifier_Device_ID_3rdParty',
    'Identifier_IMEI_3rdParty',
    'Identifier_IMSI_3rdParty',
    'Identifier_IP_Address_3rdParty',
    'Identifier_MAC_3rdParty',
    'Identifier_Mobile_Carrier_3rdParty',
    'Identifier_SIM_Serial_3rdParty',
    'Identifier_SSID_BSSID_3rdParty',
    'Location_3rdParty',
    'Location_Bluetooth_3rdParty',
    'Location_Cell_Tower_3rdParty',
    'Location_GPS_3rdParty',
    'Location_IP_Address_3rdParty',
    'Location_WiFi_3rdParty'
    ]

    for x in ThirdParyList:
        xAndPerformed = x + "\n    modality: PERFORMED"
        if xAndPerformed in text:
            print("DETECTED 3rd Party in: "+str(i)+"   Because of: "+xAndPerformed)
            return True

def splitCSV(request):
    #this reads the csv and puts it in the files
    path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\6Oct.csv"
    pos = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\Train\Positive"
    neg = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\Train\Negative"
    corpusCSV = open(path,"r")
    counter = 0;
    for line in corpusCSV.readlines():
        counter = counter+1
        if(line[0:line.find(",")] == "positive"):
            newFile = open(os.path.join(pos,str(counter)+".txt"), "w")
            newFile.write(line[line.find(",")+1:find_2nd(line,",")])
        else:
            newFile = open(os.path.join(neg,str(counter)+".txt"), "w")
            newFile.write(line[line.find(",")+1:find_2nd(line,",")])
        newFile.close()
        print(line[0:line.find(",")])

    return render(request, 'database/database.html')

def makeURLArray(request):
    path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\mitmdumps results\1pm_11_Sep_v4_Copy\requested_urls.txt"
    detectTrackersInHeaders(makeTrackingHeadersArray(), path)
    return render(request, 'database/database.html')

def find_2nd(string, substring):
   return string.find(substring, string.find(substring) + 1)

def makePPString(request):
    path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\PrivacyPolicyText\com.spartan.butt.free.txt"
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
    print(data)

def testFunction(request):
    #print(vt_uploadfile("com.tinymission.dailyyogafree"))
    uploadFileVTHannes("com.tinymission.dailyyogafree")
    #getAPKHandlesfromThesisList()
    #print(getTextFromHTML("https://www.bodygrooveondemand.com/privacy")[0])
    #PPShares3rdParty("We do not share your personal phone number with third parties. These third parties include google analytics and advertisers.")
    return render(request, 'database/health-list.html')
