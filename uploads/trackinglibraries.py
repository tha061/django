import os, sys, codecs, fnmatch, time, binascii, requests, json, sqlite3, hashlib
from bs4 import BeautifulSoup
from subprocess import call
from androguard import *
from .apk import APK


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

def vt_scan_OLD(app_id):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    api_key = '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae'
    params = {'apikey': api_key}
    #app_id = apk_path.split("/")[-1]
    apk_path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s.apk" % app_id

    files = {'file': ('%s' % app_id, open(apk_path, 'rb'))}
    try:
        response = requests.post(url, files=files, params=params)
        js = response.json()
        print(js)
        permalink = js['permalink']
        sha1 = js['sha1']
        resource = js['resource']
        response_code = js['response_code']
        scan_id = js['scan_id']
        verbose_msg = js['verbose_msg']
        sha256 = js['sha256']
        md5 = js['md5']
    except:
        permalink = "NA"
        sha1 = "NA"
        resource = "NA"
        response_code = "NA"
        scan_id = "NA"
        verbose_msg = "NA"
        sha256 = "NA"
        md5 = "NA"
    list = [permalink,sha1,resource,response_code,scan_id,verbose_msg,sha256,md5]
    return list


def getSha(app_id):
    filename = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s.apk" % app_id
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
    return readable_hash

def vt_scan(app_id):
    #this will search on virustotal by the Sha256 of the .apk file, I will need to figure out a way so that if the sha256
    #doesnt work because nobody has uploaded that .apk to VT before, then it uploads the file to VT
    url = 'https://www.virustotal.com/vtapi/v2/file/report'


    sha = str(getSha(app_id))

    params = {'apikey': '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae', 'resource':sha }


    response = requests.get(url, params=params)
    js = response.json()


    jsonPath = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\VirusTotal", app_id+"VirusTotal.txt")
    jsonFile = open(jsonPath, "w")
    json.dump(response.json(), jsonFile, indent = 2)

    try:
        permalink = js['permalink']
        sha1 = js['sha1']
        resource = js['resource']
        response_code = js['response_code']
        scan_id = js['scan_id']
        verbose_msg = js['verbose_msg']
        sha256 = js['sha256']
        md5 = js['md5']
        total = js['total']
        positives = js['positives']
    except:
        permalink = "NA"
        sha1 = "NA"
        resource = "NA"
        response_code = "NA"
        scan_id = "NA"
        verbose_msg = "NA"
        sha256 = "NA"
        md5 = "NA"
        total = "NA"
        positives = "NA"

    list = [permalink,sha1,resource,response_code,scan_id,verbose_msg,sha256,md5,total, positives]
    return list

def get_permissions(app_id):
    '''Path to AndroidManifest File'''
    #base_path = '/Users/ikr001/VPNdroid/googleplay-api/adblockingApps/xmls/%s-xml.txt'% app_id
    base_path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\AndroidManifest.xml"

    soup = BeautifulSoup(open(base_path, "rb").read(), "lxml")

    apps_all_features = {}
    feature_list = []
    try:
        for x in soup.findAll('uses-feature'):
            feature_list.append(x.attrs['android:name']+"::"+x.attrs['android:required'])
    except:
        pass

    apps_all_features.update({app_id:feature_list})

    apps_all_permissions = {}
    perm_list = []
    try:
        for x in soup.findAll('uses-permission'):
            perm_list.append(x.attrs['android:name'])

        for x in soup.findAll('service'):
            try:
                perm_list.append(x.attrs['android:permission'])
            except:
                pass
    except:
        pass

    apps_all_permissions.update({app_id:perm_list})

    return app_id, apps_all_permissions, apps_all_features
