#this .py contains all the functions for install, removing apk's from mobile device
import os
from os import chdir, system


def openEmulator(name):
    AVD = name
    os.system("emulator -avd "+AVD)

def installApp(appID):
    apkPath = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads"
    os.chdir(apkPath)
    os.system("adb install "+ appID +".apk")

def monkeyCMD(apkHandle):
    binPath = r"C:\Users\jake_\AppData\Local\Android\Sdk\tools\bin"
    os.chdir(binPath)
    cmd = "monkeyrunner script.py "+apkHandle
    print("Executing monkeyCMD")
    print(cmd)
    os.system(cmd)
    print("Finished Monkeyrunner")
    mitmdumpDecompile(apkHandle)
    #os.system()

def mitmdumpDecompile(apkHandle):
    binPath = r"C:\Users\jake_\AppData\Local\Android\Sdk\tools\bin"
    os.chdir(binPath)
    cmd = "py mitmdump_parser.py "+apkHandle
    print("Decompiling MITM Results")
    print(cmd)
    os.system(cmd)
