#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File name: download_apk.py
   Author: Dawand Sulaiman

   Download APK files from Google Play Store with Python
   This script scraps https://apkpure.com to get the apk download link
   Make sure you have BeautifulSoup and urllib libraries
"""

from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import requests
import os
import shutil
import zipfile

def search(query):
    res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                      'Version/9.1.2 Safari/601.7.5 '
    }).text
    soup = BeautifulSoup(res, "html.parser")
    search_result = soup.find('div', {'id': 'search-res'}).find('dl', {'class': 'search-dl'})
    app_tag = search_result.find('p', {'class': 'search-title'}).find('a')
    download_link = 'https://apkpure.com' + app_tag['href']
    return download_link

def checkIfXAPK(soupString):
    lowerString = soupString.lower()

    xapkPos = lowerString.find("/b/xapk")
    print("xapk Position: "+str(xapkPos))
    if xapkPos == -1:
        return False
    else:
        return True

def download(link,app_id):
    print("Split: "+link.split('/')[-1])
    print("App ID: "+app_id)
    if link.split('/')[-1] == app_id:
        res = requests.get(link + '/download?from=details', headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                          'Version/9.1.2 Safari/601.7.5 '
        }).text
        soup = BeautifulSoup(res, "html.parser").find('a', {'id': 'download_link'})

        print(checkIfXAPK(str(soup)))

        #soupString = str(soup).lower()
        #print(soupString)
        #xapkPos = soupString.find("/b/xapk")
        #print("xapk Position: "+str(xapkPos))
        #downloadPosition = soup.find("download_link")
        
        if soup['href']:
            r = requests.get(soup['href'], stream=True, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                              'Version/9.1.2 Safari/601.7.5 '
            })

            if checkIfXAPK(str(soup)):
                with open(link.split('/')[-1] + '.xapk', 'wb') as file:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)


                changeXAPKtoZIP(app_id)
                extractAPK(app_id)
                #extract .apk file
                #delete other stuff
            else:
                with open(link.split('/')[-1] + '.apk', 'wb') as file:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)


def changeXAPKtoZIP(app_id):
    xapkPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".xapk")
    apkPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".apk")
    zipPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".zip")

    os.rename(xapkPATH, zipPATH)

def extractAPK(app_id):
        xapkPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".xapk")
        apkPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".apk")
        zipPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".zip")
        with zipfile.ZipFile(zipPATH) as z:
            print(z)
            with z.open(app_id+".apk") as zf, open(apkPATH, 'wb') as f:
                shutil.copyfileobj(zf, f)

def download_apk(app_id):
    download_link = search(app_id)

    if download_link is not None:
        print('Downloading {}.apk ...'.format(download_link))
        print("download link: ")
        print(download_link)
        print(app_id)

        download(download_link, app_id)
        print('Download completed!')
    else:
        print('No results')


def checkApkDownloaded(apkCode):
    apkPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", apkCode+".apk")
    return os.path.exists(apkPATH)

# Test it
