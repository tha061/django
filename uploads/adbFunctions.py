#this .py contains all the functions for install, removing apk's from mobile device
import os
from os import chdir, system
from .functions import SaveFiletoDatabase, makeTrackingHeadersArray, detectTrackersInHeaders


def openEmulator(name):
    AVD = name
    os.system("emulator -avd "+AVD)

def installApp(appID):
    apkPath = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads"
    os.chdir(apkPath)
    os.system("adb install "+ appID +".apk")

def monkeyCMD(apkHandle, instance):
    binPath = r"C:\Users\jake_\AppData\Local\Android\Sdk\tools\bin"
    os.chdir(binPath)
    cmd = "monkeyrunner script.py "+apkHandle
    print("Executing monkeyCMD")
    print(cmd)
    os.system(cmd)
    print("Finished Monkeyrunner")
    #mitmdumpDecompile(apkHandle, instance)
    #os.system()

def mitmdumpDecompile(apkHandle, instance):
    binPath = r"C:\Users\jake_\AppData\Local\Android\Sdk\tools\bin"
    os.chdir(binPath)
    cmd = "py mitmdump_parser.py "+apkHandle
    print("Decompiling MITM Results")

    print(cmd)
    os.system(cmd)

    URLSPath = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\mitmdumps results\%s\%s_requested_urls.txt" % (apkHandle, apkHandle)
    detectTrackersInHeaders(makeTrackingHeadersArray(),URLSPath, apkHandle)

    if(os.path.exists(URLSPath)):
        SaveFiletoDatabase(URLSPath, "URLS", instance, apkHandle)
    else:
        print("No Network Traffic at all Detected")

    Sharing_URLS_Path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\requested_urls_sharing\%s.txt" % apkHandle
    if(os.path.exists(Sharing_URLS_Path)):
        SaveFiletoDatabase(Sharing_URLS_Path, "TrackingURLS", instance, apkHandle)
    else:
        print("No Sharing URLS Detected")
