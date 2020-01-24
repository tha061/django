import os, sys, codecs, fnmatch, time, binascii, requests, json, sqlite3
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

def vt_scan(app_id):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    api_key = '8e964db7706daa35e71df310ce68944393a8c254a9c9e7a6a1583ee479a4142a'
    params = {'apikey': api_key}
    #app_id = apk_path.split("/")[-1]
    apk_path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\%s.apk" % app_id

    files = {'file': ('%s' % app_id, open(apk_path, 'rb'))}
    try:
        response = requests.post(url, files=files, params=params)
        js = response.json()

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
    list = permalink,sha1,resource,response_code,scan_id,verbose_msg,sha256,md5
    return list

def get_permissions(app_id):
    '''Path to AndroidManifest File'''
    #base_path = '/Users/ikr001/VPNdroid/googleplay-api/adblockingApps/xmls/%s-xml.txt'% app_id
    base_path = './%s/AndroidManifest.xml'% app_id

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
