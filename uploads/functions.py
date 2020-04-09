import os
from os import chdir, system
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import pandas as pd
import requests
import shutil






def returnZ(str):
    return str[0]

def decompileAPK(code, folder, folderCD):
    os.chdir(folder)
    os.system("cd "+folderCD)
    os.system("apktool d "+code+".apk ./"+code+".apk")

def getLibrariesDirectories(app_id):

    path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\smali"%app_id
    apps_libraries = {}

    libraries = []


    for path,subdir,files in os.walk(path):

       for name in subdir:

           libraries.append(name)
       #break        "include the break if you only want the first layer"

    return libraries

def getLibrariesSmali(app_id):

    path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\smali"%app_id
    apps_libraries = {}

    libraries = []


    for path,subdir,files in os.walk(path):

       for name in files:

           libraries.append(name)

    return libraries


def getLibraries2(app_id):
    smali_path  = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s"%app_id

    base_path = r"\smali"

    os.chdir(smali_path)

    apps_libraries = {}

    libraries = []
    try:

        for item in os.walk(base_path).next()[1]:
            if len(os.walk(base_path+"/%s"%item).next()[1]) == 0:
                libraries.append(item)
            for x in os.walk(base_path+"/%s"%item).next()[1]:
                libraries.append(item+"/"+x)
    except:
        pass

    apps_libraries.update({app_id:libraries})

    return app_id, apps_libraries


def usesLibraryFromXML(manifestPATH):
    permissionList = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("uses-library")

    for perm in permissions:

        for att in perm.attrib:
            permissionList.append(perm.attrib[att])

    return permissionList

def usesPermissionsFromXML(manifestPATH):

    permissionList = []
    permissionListLevel = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("uses-permission")

    for perm in permissions:
        for att in perm.attrib:
            permissionList.append(perm.attrib[att])


    diction = getPermissionsDictionary()
    for perm in permissionList:
        finalPerm = perm.rfind(".")
        actualPermission = perm[1+finalPerm:]
        if actualPermission in diction:
            new = perm+" Protection Level: "+diction[actualPermission]
        else:
            new = perm+" Protection Level: Developer Defined Permission"
        permissionListLevel.append(new)
    return permissionListLevel

def permissionsFromXML(manifestPATH):
    permissionList = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("permission")

    for perm in permissions:

        concat = ""
        for att in perm.attrib:

            #position = att.rfind("}")
            splitAtt = att.split("}")
            cleanAtt = splitAtt[1]

            concat = concat + "   "+ cleanAtt + ": " +perm.attrib[att]

        permissionList.append(concat)
    return permissionList

def servicesFromXML(manifestPATH):

    base_path = manifestPATH

    soup = BeautifulSoup(open(base_path, "rb").read(), "lxml")

    apps_all_features = {}
    feature_list = []


    apps_all_permissions = {}
    perm_list = []

    for x in soup.findAll('service'):

        permission = ""
        try:
            name = x.attrs['android:name']
        except:
            pass

        try:
            permission = x.attrs['android:permission']
        except:
            pass

        nameAndPerm =  "name: "+ name+ "  permission: "+permission
        try:
            perm_list.append(nameAndPerm)
        except:
            pass
        name = ""
        permission =""
        nameAndPerm =""


    app_id = "Service and Permissions"
    apps_all_permissions.update({app_id:perm_list})

    return apps_all_permissions

def download_apk(package, version_code, output_path):
    """
    :param package: app's package, e.g. com.android.chrome
    :param version_code: which version of the app you want to download
    :param output_path: where to save the apk file
    """
    try:
        # warning: we must emulate an ATOMIC write to avoid unfinished files.
        # To do so, we use the os.rename() function that should always be atomic under
        # certain conditions (https://linux.die.net/man/2/rename)
        data = play_store.download(package, version_code)
        if not data:
            return
        with open(output_path + ".temp", "wb") as f:
            f.write(data)
        os.rename(output_path + ".temp", output_path)
    except DownloadError as e:
        logging.error(str(e))

def getManifest(path):
    with ZipFile(path, 'r') as zipObj:
   # Get a list of all archived file names from the zip
        listOfFileNames = zipObj.namelist()

        zipObj.extract("AndroidManifest.xml", r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads")
   # Iterate over the file names
        #for fileName in listOfFileNames:
       # Check filename endswith csv
            #if fileName.endswith('.xml'):
           # Extract a single file from zip
                #zipObj.extract(fileName, 'temp_csv')



def getPermissionLevels():

    URL = "https://developer.android.com/reference/android/Manifest.permission"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all("div",{"data-version-added":True})

    permissionName = []
    ApiLevel = []
    permissionLevel = []
    #test = result[1].find("a",{"href": "/guide/topics/manifest/uses-sdk-element#ApiLevels"}).get_text(separator=" ").strip()
    for x in range(len(result)):
        permissionName.append(result[x].find("h3",{"class": "api-name"}).get_text(separator=" ").strip()) #gets permission name

        test = result[x].find("p").get_text(separator=" ").strip()    #if statement gets protectional level
        if(test.find("Protection level: ") != -1):
            position = test.find("Protection level: ")+18
            gap = test.find(" ",position+1)
            word = test[position:gap]
            word.replace(r"\n", "") #html file contains \n, removes \n

            if(gap == -1):  #if statement fixes issue about not including last char of string
                permissionLevel.append(word+test[gap])
            else:
                permissionLevel.append(word)
        else:
            permissionLevel.append("N/A")


    dictionary = dict(zip(permissionName, permissionLevel))  #returns a dictionary too look up permissions and it will tell you their level
    #print(dictionary)
    return dictionary

def getPermissionsDictionary():
    dictionary = {'ACCEPT_HANDOVER': 'dangerous', 'ACCESS_BACKGROUND_LOCATION': 'dangerous\n', 'ACCESS_CALL_AUDIO': 'signature|appop', 'ACCESS_CHECKIN_PROPERTIES': 'N/A',
     'ACCESS_COARSE_LOCATION': 'dangerous', 'ACCESS_FINE_LOCATION': 'dangerous', 'ACCESS_LOCATION_EXTRA_COMMANDS': 'normal', 'ACCESS_MEDIA_LOCATION': 'dangerous',
     'ACCESS_NETWORK_STATE': 'normal', 'ACCESS_NOTIFICATION_POLICY': 'normal', 'ACCESS_WIFI_STATE': 'normal', 'ACCOUNT_MANAGER': 'N/A', 'ACTIVITY_RECOGNITION': 'dangerous',
     'ADD_VOICEMAIL': 'dangerous', 'ANSWER_PHONE_CALLS': 'dangerous', 'BATTERY_STATS': 'signature|privileged|development', 'BIND_ACCESSIBILITY_SERVICE': 'signature',
     'BIND_APPWIDGET': 'N/A', 'BIND_AUTOFILL_SERVICE': 'signature', 'BIND_CALL_REDIRECTION_SERVICE': 'signature|privileged',
     'BIND_CARRIER_MESSAGING_CLIENT_SERVICE': 'signature', 'BIND_CARRIER_MESSAGING_SERVICE': 'N/A', 'BIND_CARRIER_SERVICES': 'signature|privileged',
     'BIND_CHOOSER_TARGET_SERVICE': 'signature', 'BIND_CONDITION_PROVIDER_SERVICE': 'signature', 'BIND_CONTROLS': 'N/A', 'BIND_DEVICE_ADMIN': 'signature',
     'BIND_DREAM_SERVICE': 'signature', 'BIND_IN_CALL_SERVICE': 'signature|privileged', 'BIND_INPUT_METHOD': 'signature', 'BIND_MIDI_DEVICE_SERVICE': 'signature',
     'BIND_NFC_SERVICE': 'signature', 'BIND_NOTIFICATION_LISTENER_SERVICE': 'signature', 'BIND_PRINT_SERVICE': 'signature', 'BIND_QUICK_ACCESS_WALLET_SERVICE': 'signature',
     'BIND_QUICK_SETTINGS_TILE': 'N/A', 'BIND_REMOTEVIEWS': 'signature|privileged', 'BIND_SCREENING_SERVICE': 'signature|privileged',
     'BIND_TELECOM_CONNECTION_SERVICE': 'signature|privileged', 'BIND_TEXT_SERVICE': 'signature', 'BIND_TV_INPUT': 'signature|privileged',
     'BIND_VISUAL_VOICEMAIL_SERVICE': 'signature|privileged', 'BIND_VOICE_INTERACTION': 'signature', 'BIND_VPN_SERVICE': 'signature', 'BIND_VR_LISTENER_SERVICE': 'signature',
     'BIND_WALLPAPER': 'signature|privileged', 'BLUETOOTH': 'normal', 'BLUETOOTH_ADMIN': 'normal', 'BLUETOOTH_PRIVILEGED': 'N/A', 'BODY_SENSORS': 'dangerous',
     'BROADCAST_PACKAGE_REMOVED': 'N/A', 'BROADCAST_SMS': 'N/A', 'BROADCAST_STICKY': 'normal', 'BROADCAST_WAP_PUSH': 'N/A', 'CALL_COMPANION_APP': 'normal',
     'CALL_PHONE': 'dangerous', 'CALL_PRIVILEGED': 'N/A', 'CAMERA': 'dangerous', 'CAPTURE_AUDIO_OUTPUT': 'N/A', 'CHANGE_COMPONENT_ENABLED_STATE': 'N/A',
     'CHANGE_CONFIGURATION': 'signature|privileged|development', 'CHANGE_NETWORK_STATE': 'normal', 'CHANGE_WIFI_MULTICAST_STATE': 'normal', 'CHANGE_WIFI_STATE': 'normal',
     'CLEAR_APP_CACHE': 'signature|privileged', 'CONTROL_LOCATION_UPDATES': 'N/A', 'DELETE_CACHE_FILES': 'signature|privileged', 'DELETE_PACKAGES': 'N/A',
     'DIAGNOSTIC': 'N/A', 'DISABLE_KEYGUARD': 'normal', 'DUMP': 'N/A', 'EXPAND_STATUS_BAR': 'normal', 'FACTORY_TEST': 'N/A', 'FOREGROUND_SERVICE': 'normal',
     'GET_ACCOUNTS': 'dangerous', 'GET_ACCOUNTS_PRIVILEGED': 'signature|privileged', 'GET_PACKAGE_SIZE': 'normal', 'GET_TASKS': 'N/A',
     'GLOBAL_SEARCH': 'signature|privileged', 'INSTALL_LOCATION_PROVIDER': 'N/A', 'INSTALL_PACKAGES': 'N/A', 'INSTALL_SHORTCUT': 'normal',
     'INSTANT_APP_FOREGROUND_SERVICE': 'signature|development|instant|appop', 'INTERACT_ACROSS_PROFILES': 'N/A', 'INTERNET': 'normal', 'KILL_BACKGROUND_PROCESSES': 'normal',
     'LOADER_USAGE_STATS': 'signature|privileged|appop', 'LOCATION_HARDWARE': 'N/A', 'MANAGE_DOCUMENTS': 'N/A', 'MANAGE_EXTERNAL_STORAGE': 'signature|appop|preinstalled',
     'MANAGE_OWN_CALLS': 'normal', 'MASTER_CLEAR': 'N/A', 'MEDIA_CONTENT_CONTROL': 'N/A', 'MODIFY_AUDIO_SETTINGS': 'normal', 'MODIFY_PHONE_STATE': 'N/A',
     'MOUNT_FORMAT_FILESYSTEMS': 'N/A', 'MOUNT_UNMOUNT_FILESYSTEMS': 'N/A', 'NFC': 'normal', 'NFC_PREFERRED_PAYMENT_INFO': 'normal', 'NFC_TRANSACTION_EVENT': 'normal',
     'PACKAGE_USAGE_STATS': 'signature|privileged|development|appop|retailDemo', 'PERSISTENT_ACTIVITY': 'N/A', 'PROCESS_OUTGOING_CALLS': 'dangerous',
     'QUERY_ALL_PACKAGES': 'N/A', 'READ_CALENDAR': 'dangerous', 'READ_CALL_LOG': 'dangerous\n', 'READ_CONTACTS': 'dangerous', 'READ_EXTERNAL_STORAGE': 'dangerous',
     'READ_INPUT_STATE': 'N/A', 'READ_LOGS': 'N/A', 'READ_PHONE_NUMBERS': 'dangerous', 'READ_PHONE_STATE': 'dangerous', 'READ_PRECISE_PHONE_STATE': 'N/A',
     'READ_SMS': 'dangerous\n', 'READ_SYNC_SETTINGS': 'normal', 'READ_SYNC_STATS': 'normal', 'READ_VOICEMAIL': 'signature|privileged', 'REBOOT': 'N/A',
     'RECEIVE_BOOT_COMPLETED': 'normal', 'RECEIVE_MMS': 'dangerous\n', 'RECEIVE_SMS': 'dangerous\n', 'RECEIVE_WAP_PUSH': 'dangerous\n', 'RECORD_AUDIO': 'dangerous',
     'REORDER_TASKS': 'normal', 'REQUEST_COMPANION_RUN_IN_BACKGROUND': 'normal', 'REQUEST_COMPANION_USE_DATA_IN_BACKGROUND': 'normal', 'REQUEST_DELETE_PACKAGES': 'normal',
     'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS': 'normal', 'REQUEST_INSTALL_PACKAGES': 'signature', 'REQUEST_PASSWORD_COMPLEXITY': 'normal', 'RESTART_PACKAGES': 'N/A',
     'SEND_RESPOND_VIA_MESSAGE': 'N/A', 'SEND_SMS': 'dangerous\n', 'SET_ALARM': 'normal', 'SET_ALWAYS_FINISH': 'N/A', 'SET_ANIMATION_SCALE': 'N/A', 'SET_DEBUG_APP': 'N/A',
     'SET_PREFERRED_APPLICATIONS': 'N/A', 'SET_PROCESS_LIMIT': 'N/A', 'SET_TIME': 'N/A', 'SET_TIME_ZONE': 'N/A', 'SET_WALLPAPER': 'normal', 'SET_WALLPAPER_HINTS': 'normal',
     'SIGNAL_PERSISTENT_PROCESSES': 'N/A', 'SMS_FINANCIAL_TRANSACTIONS': 'signature|appop', 'START_VIEW_PERMISSION_USAGE': 'signature|installer', 'STATUS_BAR': 'N/A',
     'SYSTEM_ALERT_WINDOW': 'signature|preinstalled|appop|pre23|development', 'TRANSMIT_IR': 'normal', 'UNINSTALL_SHORTCUT': 'N/A', 'UPDATE_DEVICE_STATS': 'N/A',
     'USE_BIOMETRIC': 'normal', 'USE_FINGERPRINT': 'normal', 'USE_FULL_SCREEN_INTENT': 'normal', 'USE_SIP':'dangerous', 'VIBRATE': 'normal', 'WAKE_LOCK': 'normal',
     'WRITE_APN_SETTINGS': 'N/A', 'WRITE_CALENDAR': 'dangerous', 'WRITE_CALL_LOG': 'dangerous\n', 'WRITE_CONTACTS': 'dangerous',
     'WRITE_EXTERNAL_STORAGE': 'dangerous', 'WRITE_GSERVICES': 'N/A', 'WRITE_SECURE_SETTINGS': 'N/A', 'WRITE_SETTINGS': 'signature|preinstalled|appop|pre23',
     'WRITE_SYNC_SETTINGS': 'normal', 'WRITE_VOICEMAIL': 'signature|privileged'}
    return dictionary

def mergeLists(listA, listB):
    result = {}
    for a in listA:
        for b in listB:

            #print("b: "+b)
            editedString = b.replace(a+" ", "")
            if(a == "Installs"):
                editedString = editedString.replace(",","")
                editedString = editedString.replace("+","")

            if(a == "Installs" and int(editedString) < 1000001):
                editedString = editedString + ", Warning: Low amount of users"
            #print("edited: "+editedString)
            result[a] = editedString
            listB.remove(b)
            break
    return result


def getDeveloperLinks(soup):

    string = ""
    for test in soup.find_all("div",{"class":"hAyfc"}):
        stringTest = str(test)
        print(stringTest)

        DeveloperWebsite = ""
        DeveloperEmail = ""
        PrivacyPolicy = ""

        if "<div class=\"BgcNfc\">Developer" in stringTest:
            if stringTest.find("hrTbp\" href=") > 1:
                websitePos = stringTest.find(">Visit website")
                QuoteLast = stringTest.rfind('\"',0,websitePos)
                print(QuoteLast)
                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)
                print(QuoteSecond)
                DeveloperWebsite = stringTest[QuoteSecond+1:QuoteLast]

            if stringTest.find("hrTbp euBY6b\" href=") > 1:
                websitePos = stringTest.find("hrTbp euBY6b\" href=")+27
                endWebPost =stringTest.find('"',websitePos+2)
                print("web pos: "+str(websitePos))
                print("end web pos: "+str(endWebPost))
                DeveloperEmail = stringTest[websitePos:endWebPost]

            if stringTest.find(">Privacy Policy") > 1:
                PrivacyPos = stringTest.find(">Privacy Policy")
                print(PrivacyPos)
                QuoteLast = stringTest.rfind('\"',0,PrivacyPos)
                print(QuoteLast)
                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)
                print(QuoteSecond)
                PrivacyPolicy = stringTest[QuoteSecond+1:QuoteLast]
                #now i need to find last two substrings before PrivacyPos (" " "), and get the reference there

        print(DeveloperWebsite)
        print(DeveloperEmail)
        print(PrivacyPolicy)
        links = {"Developer Website":DeveloperWebsite,"Developer Email":DeveloperEmail,"Privacy Policy":PrivacyPolicy}


    return links

def metaFromWebsite(appID):
    URL = "https://play.google.com/store/apps/details?id="+appID+"&hl=en_AU"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    links = getDeveloperLinks(soup)

    print("LINKS....")
    print(links)

    titleForResult = [e.get_text(separator=" ").strip() for e in soup.find_all("div",{"class":"BgcNfc"})]
    result = [e.get_text(separator=" ").strip() for e in soup.find_all("div",{"class":"hAyfc"})]
    rating = soup.find("div",{"class":"BHMmbe"}).get_text(separator=" ").strip()
    if(float(rating) < 3.0):
        rating = rating + ", Warning: Low rated application"
    description = soup.find("div",{"class":"DWPxHb"}).get_text(separator=" ").strip()

    Meta = []
    #Meta.append(titleForResult)
    #Meta.append(result)
    Meta.append(mergeLists(titleForResult, result))
    Meta.append(rating)
    Meta.append(description)
    Meta.append(links)

    print(Meta)

    return Meta

    #with open(File_URL, 'w', encoding='utf-8') as f_out: COMMENTED OUT 31 MARCH 2020
    #    f_out.write(soup.prettify())


def makeCertificateFile(appID):
    apkFolder = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads",appID)
    CertFolder = os.path.join(apkFolder,   r"original\META-INF")
    CertFile = r"original\META-INF\%sCertFile.txt" %(appID)
    apkCertFile = os.path.join(apkFolder, CertFile)
    certificateFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\certificate"
    os.chdir(CertFolder)
    systemString = "openssl pkcs7 -inform DER -in CERT.RSA -out "+appID+"CertFile.txt  -print_certs -text"
    os.system(systemString)
    shutil.copy(apkCertFile, certificateFolder)
    #os.chdir(apkFolder)



class APKAnalysis():
    def __init__(self, name="", fileSize="", VTmd5="", VTmsg="", VTpermalink="", VTresource="", VTresponsecode="", VTscanID="",
    VTsha1="", VTsha256="",usesPermissions = "", permissions = "", metaData ="", rating="", description="", service=""):
        self.name = name
        self.fileSize = fileSize
        self.VTmd5 = VTmd5
        self.VTmsg = VTmsg
        self.VTpermalink = VTpermalink
        self.VTresource = VTresource
        self.VTresponsecode = VTresponsecode
        self.VTscanID = VTscanID
        self.VTsha1 = VTsha1
        self.VTsha256 = VTsha256
        self.usesPermissions = usesPermissions
        self.permissions = permissions
        self.service = service
        self.metaData = metaData
        self.rating = rating
        self.description = description
