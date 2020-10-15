#this .py contains all the functions for install, removing apk's from mobile device
import os
from os import chdir, system
from .functions import SaveFiletoDatabase, makeTrackingHeadersArray, detectTrackersInHeaders
from .filepaths import *


def openEmulator(name):
    AVD = name
    os.system("emulator -avd "+AVD)

def installApp(appID):
    apkPath = filepaths_APKFolder
    os.chdir(apkPath)
    os.system("adb install "+ appID +".apk")

def monkeyCMD(apkHandle, instance):
    binPath = filepaths_AndroidMonkeyBin
    os.chdir(binPath)
    cmd = "monkeyrunner script.py "+apkHandle
    print("Executing monkeyCMD")
    print(cmd)
    os.system(cmd)
    print("Finished Monkeyrunner")
    #mitmdumpDecompile(apkHandle, instance)
    #os.system()

def mitmdumpDecompile(apkHandle, instance):
    binPath = filepaths_AndroidMonkeyBin
    os.chdir(binPath)
    cmd = "py mitmdump_parser.py "+apkHandle
    print("Decompiling MITM Results")

    print(cmd)
    os.system(cmd)

    URLSPath = returnURLSRequestedPath(apkHandle)
    #detectTrackersInHeaders(makeTrackingHeadersArray(),URLSPath, apkHandle)

    if(os.path.exists(URLSPath)):
        SaveFiletoDatabase(URLSPath, "URLS", instance, apkHandle)
    else:
        print("No Network Traffic at all Detected")

    Sharing_URLS_Path = returnURLSRequestedSharingPath(apkHandle)
    if(os.path.exists(Sharing_URLS_Path)):
        SaveFiletoDatabase(Sharing_URLS_Path, "TrackingURLS", instance, apkHandle)
    else:
        print("No Sharing URLS Detected")
