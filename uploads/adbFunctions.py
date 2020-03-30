#this .py contains all the functions for install, removing apk's from mobile device
import os
from os import chdir, system


def openEmulator():
    AVD = "Pixel_3_API"
    os.system("emulator -avd "+AVD)

def installApp(appID):
    apkPath = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads"
    os.chdir(apkPath)
    os.system("adb install "+ appID +".apk")

def monkeyCMD():
    binPath = r"C:\Users\jake_\AppData\Local\Android\Sdk\tools\bin"
    os.chdir(binPath)
    os.chdir(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\uploads")
    os.system("monkeyrunner monkeyscript.py")
    #os.system()
