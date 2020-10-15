import os
from os import chdir, system
import sys

filepaths_APKFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads"
filepaths_APKList = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\media\APK_List\ManyApks.txt"
filepaths_ResultsCSV = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\results.csv"
filepaths_returnAPKPathCD = r"Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownload"
filepaths_CERTFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\certificate"
filepaths_CertPemFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\Cert Pem Files"
filepaths_GeneralTrackingURLS = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\urlHeaderTextFiles\GeneralTrackingSystems.txt"
filepaths_thesisList = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\ThesisStuff\thesisList.txt"
filepaths_ManyAPKList = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\media\APK_List\ManyApks.txt"
filepaths_AndroidMonkeyBin = r"C:\Users\jake_\AppData\Local\Android\Sdk\tools\bin"
filepaths_NeuralNetworkModel = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\Scikit_Model\finalized_model_91_percent.sav'

filepaths_path = r""

def returnPolicyPath(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\PrivacyPolicyText", app_id+".txt")

def returnURLSRequestedPath(app_id):
    return r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\mitmdumps results\%s\%s_requested_urls.txt"%(app_id, app_id)

def returnURLSRequestedSharingPath(app_id):
    return r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\requested_urls_sharing\%s.txt"%app_id

def returnAPKPath(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".apk")

def returnAPKFolder(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id)

def returnPolicyPath(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\PrivacyPolicyText", app_id+".txt")

def returnAPKManifestPath(app_id):
    return r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\AndroidManifest.xml"%app_id


def returnAPKZIP(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".zip")

def returnXAPKZIP(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".xapk")


def returnAPKJSON(app_id):
    return  os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder", app_id+"JSONFile.txt")

def returnAPKVirusTotal(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\VirusTotal", app_id+"VirusTotal.txt")

def returnAPKCERT(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\certificate", app_id+"CertFile.txt")

def returnAPKMitmdumps(app_id):
    return r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\mitmdumps\%s"%app_id

def returnAPKSmaliFolder(app_id):
    return r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\smali"%app_id

def returnAPKDecomile_re(app_id):
    return r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads" + apk_name + "_re"

def returnVirusTotalUploadFileResults(app_id):
    return os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\VTHannes", app_id+".txt")
