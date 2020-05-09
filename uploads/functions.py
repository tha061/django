import os
from os import chdir, system
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import pandas as pd
import requests
import shutil
from django.core.files.base import ContentFile

def returnZ(str):
    return str[0]

def decompileAPK(code, folder, folderCD):
    os.chdir(folder)
    os.system("cd "+folderCD)
    os.system("apktool d "+code+".apk ./"+code+".apk")

def apkToZip(folder, code):
    os.chdir(folder)
    codeAPK = code + ".apk"
    codeZIP = code + ".zip"

    os.rename(codeAPK, codeZIP)

    with ZipFile(codeZIP, 'r') as zipObj:
   # Extract all the contents of zip file in current directory
        zipObj.extractall(code)

def getLibrariesDirectories(app_id):

    paths = getSmaliFolders(app_id)
    #path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\smali"%app_id


    apps_libraries = {}

    libraries = []

    for path in paths:
        shortenedPathPosition = path.find("smali")
        for root,dirs,files in os.walk(path):
            if not dirs:
                shortenedPath = str(root[shortenedPathPosition+6:]).replace(r'\\','/')
                noSlash = shortenedPath.replace('\\', '/')
                libraries.append(noSlash)
           #break        "include the break if you only want the first layer"

    return libraries

def SmaliToDict():
    smaliTextPath = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\Smali List\apps_libraries.txt'
    smaliDictPath = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\Smali List\smaliDict.txt'
    d = {}
    with open(smaliTextPath) as f:
        for line in f:

            lineSplit = line.split("\t")
            lineSplit[2] = lineSplit[2][:-1]
            tuple = (lineSplit[1], lineSplit[2])
            d[lineSplit[0]] = tuple



def returnSmaliTuplDict():
    d = {'Library': ('AdlibraryPath', 'Category'), 'Admob': ('com/admob', 'Targeted ads'), 'Facebook': ('com/facebook', 'Social networking service'), 'Flurry'
: ('com/flurry', 'Analytics'), 'Twitter4j': ('com/twitter4j', 'Social networking service'), 'Jsoup': ('com/jsoup', 'Utility'), 'Revmob': ('com/revmob'
, 'Targeted ads'), 'Millennialmedia': ('com/millennialmedia', 'Targeted ads'), 'Nostra13': ('com/nostra13', 'Utility'), 'Inmobi': ('com/inmobi',
'Targeted ads'), 'Acra': ('com/acra', 'Utility'), 'Unity3d': ('com/unity3d', 'Game engine'), 'Oauth': ('com/oauth', 'Utility'), 'Ksoap2': ('com/ksoap2',
'Utility'), 'Chartboost': ('com/chartboost', 'Targeted ads'), 'Paypal': ('com/paypal', 'Payment'), 'Bugsense': ('com/bugsense', 'Utilities'), 'Qbiki': (
'com/qbiki', 'Development aid'), 'Loopj': ('com/loopj', 'Utility'), 'Adobe': ('com/adobe', 'Utility'), 'Phonegap': ('com/phonegap', 'Utility'),
'Biznessapps': ('com/biznessapps', 'Development aid'), 'Smaato': ('com/smaato', 'Targeted ads'), 'Codehaus': ('com/codehaus', 'Utility'), 'Mopub':
('com/mopub', 'Targeted ads'), 'Urbanairship': ('com/urbanairship', 'Payment'), 'Kawa': ('com/kawa', 'Utility'), 'Adwhirl': ('com/adwhirl', 'Targeted ads'),
'Appbrain': ('com/appbrain', 'Utility'), 'Umeng': ('com/umeng', 'Mobile analytics'), 'Adfonic': ('com/adfonic', 'Targeted ads'), 'Titanium':
('com/titanium', 'Development aid'), 'Appcelerator': ('com/appcelerator', 'Utility'), 'Ansca': ('com/ansca', 'Utility'), 'Tapjoy': ('com/tapjoy', 'Targeted ads')
, 'Applovin': ('com/applovin', 'Targeted ads'), 'Amazon': ('com/amazon/analytics', 'Mobile analytics'), 'Badlogic': ('com/badlogic', 'Game engine'),
'Jumptap': ('com/jumptap', 'Targeted ads'), 'Crittercism': ('com/crittercism', 'Utility'), 'Mobclix': ('com/mobclix', 'Targeted ads'), 'Playhaven':
('com/playhaven', 'Targeted ads'), 'Inneractive': ('com/inneractive', 'Targeted ads'), 'Appmk': ('com/appmk', 'Utility'), 'Tencent': ('com/tencent',
'Targeted ads'), 'Andengine': ('com/andengine', 'Social gaming'), 'Baidu': ('com/baidu/location', 'Targeted ads'), 'Appyet': ('com/appyet',
'Development aid'), 'Osmdroid': ('com/osmdroid', 'Utility'), 'Anywheresoftware': ('com/anywheresoftware', 'Utility'), 'Scribe': ('com/scribe', 'Content provider'),
'Heyzap': ('com/heyzap', 'Social gaming'), 'Localytics': ('com/localytics', 'Analytics'), 'Anddev': ('com/anddev', 'Utility'), 'Mixpanel':
('com/mixpanel', 'Mobile analytics'), 'Greystripe': ('com/greystripe', 'Targeted ads'), 'Amazonaws': ('com/amazonaws', 'Utility'),
'Qualcomm': ('com/qualcomm', 'Utility'), 'Cocos2dx': ('com/cocos2dx', 'Game engine'), 'Roboguice': ('com/roboguice', 'Utility'), 'Mozilla': ('com/mozilla', 'Utility'),
'Springframework': ('com/springframework', 'Utility'), 'Nuance': ('com/nuance', 'Utility'), 'Mobfox': ('com/mobfox', 'Targeted ads'), 'Openfeint':
('com/openfeint', 'Game engine'), 'Apsalar': ('com/apsalar', 'Analytics'), 'Actionbarsherlock': ('com/actionbarsherlock', 'Utility'), 'Airpush':
('com/airpush', 'Targeted ads'), 'Admarvel': ('com/admarvel', 'Targeted ads'), 'Mdotm': ('com/mdotm', 'Targeted ads'), 'Github': ('com/github', 'Utility'),
'Tapfortap': ('com/tapfortap', 'Targeted ads'), 'Apperhand': ('com/apperhand', 'Targeted ads'), 'Scoreloop': ('com/scoreloop', 'Social gaming'),
'Comscore': ('com/comscore', 'Analytics'), 'Mediba': ('com/mediba', 'Targeted ads'), 'Weibo': ('com/weibo', 'Social networking service'),
 'Twitter': ('com/twitter', 'Social networking service'), 'Zestadz': ('com/zestadz', 'Targeted ads'), 'Mcsoxford': ('com/mcsoxford', 'Utility'),
 'Nbpcorp': ('com/nbpcorp', 'Targeted ads'), 'Adknowledge': ('com/adknowledge', 'Targeted ads'), 'Mobclick': ('com/mobclick', 'Mobile analytics'), 'Zong': ('com/zong', 'Payment'), 'Htmlcleaner': ('com/htmlcleaner', 'Utility'), 'Mapsforge': ('com/mapsforge', 'Content provider'), 'Socialize': ('com/socialize', 'Social networking service')
, 'Wiyun': ('com/wiyun', 'Social gaming'), 'Dom4j': ('com/dom4j', 'Utility'), 'Cauly': ('com/cauly', 'Targeted ads'), 'Bouncycastle': ('com/bouncycastle', 'Utility'), 'Smartadserver': ('com/smartadserver', 'Targeted ads'), 'Ormma': ('com/ormma', 'Targeted ads'), 'Winterwell': ('com/winterwell', 'Social networking service'), 'Sponsorpay': ('com/sponsorpay', 'Targeted ads'), 'Omniture': ('com/omniture', 'Mobile analytics'), 'Kenai': ('com/kenai', 'Development aid'), 'Dropbox': ('com/dropbox', 'Utility'), 'Leadbolt': ('com/leadbolt', 'Targeted ads'), 'Fedorvlasov': ('com/fedorvlasov', 'Utility'),
 'Mocoplex': ('com/mocoplex', 'Targeted ads'), 'Brightcove': ('com/brightcove', 'Content provider'), 'Alipay': ('com/alipay', 'Payment'), 'Greendroid'
: ('com/greendroid', 'Development aid'), 'Ccil': ('com/ccil', 'Utility'), 'Adwo': ('com/adwo', 'Targeted ads'), 'Commonsware': ('com/commonsware',
'Utility'), 'Aviary': ('com/aviary', 'Utility'), 'Vpon': ('com/vpon', 'Targeted ads'), 'Swarmconnect': ('com/swarmconnect', 'Targeted ads'),
'Spongycastle': ('com/spongycastle', 'Utility'), 'Iflytek': ('com/iflytek', 'Utility'), 'Pontiflex': ('com/pontiflex', 'Targeted ads'), 'Mobisage':
('com/mobisage', 'Targeted ads'), 'Papaya': ('com/papaya', 'Social gaming'), 'Xtify': ('com/xtify', 'Targeted ads'), 'Burstly': ('com/burstly', 'Targeted ads'),
 'Ideaworks3d': ('com/ideaworks3d', 'Utility'), 'Nullwire': ('com/nullwire', 'Utility'), 'Inapp': ('com/inapp', 'Utility'), 'Getjar': ('com/getjar',
 'Secondary market'), 'Webtrends': ('com/webtrends', 'Mobile analytics'), 'Livestream': ('com/livestream', 'Content provider'), 'Vervewireless':
 ('com/vervewireless', 'Targeted ads'), 'Gamesalad': ('com/gamesalad', 'Game engine'), 'Adchina': ('com/adchina', 'Targeted ads'), 'Yume': ('com/yume',
 'Targeted ads'), 'Rosaloves': ('com/rosaloves', 'Utility'), 'Nexage': ('com/nexage', 'Targeted ads'), 'Googlecode': ('com/googlecode', 'Development aid'),
 'Ngigroup': ('com/ngigroup', 'Targeted ads'), 'Cocos2d': ('com/cocos2d', 'Game engine'), 'Jcifs': ('com/jcifs', 'Utility'), 'Madhouse': ('com/madhouse',
 'Targeted ads'), 'Sonicnotify': ('com/sonicnotify', 'Targeted ads'), 'Everbadge': ('com/everbadge', 'Targeted ads'), 'Pjsip': ('com/pjsip', 'Utility'),
'Fmod': ('com/fmod', 'Utility'), 'Bumptech': ('com/bumptech', 'Utility'), 'Qwapi': ('com/qwapi', 'Targeted ads'), 'Medialets': ('com/medialets',
'Targeted ads'), 'Renren': ('com/renren', 'Social networking service'), 'Eclipse': ('com/eclipse', 'Utility'), 'Vdopia': ('com/vdopia', 'Targeted ads'),
'Rhythmnewmedia': ('com/rhythmnewmedia', 'Targeted ads'), 'Suizong': ('com/suizong', 'Targeted ads'), 'Adview': ('com/adview', 'Targeted ads'),
'Devsmart': ('com/devsmart', 'Ui component'), 'Wooboo': ('com/wooboo', 'Targeted ads'), 'Twitterapime': ('com/twitterapime', 'Social networking service'),
'Jboss': ('com/jboss', 'Utility'), 'Noqoush': ('com/noqoush', 'Targeted ads'), 'Opencv': ('com/opencv', 'Utility'), 'Fiksu': ('com/fiksu', 'Targeted ads'
), 'Adserver': ('com/adserver', 'Targeted ads'), 'Microsoft': ('com/microsoft/Targeted ads', 'Targeted ads'), 'Admogo': ('com/admogo', 'Targeted ads')
, 'Groovy': ('com/groovy', 'Development aid'), 'Htmlparser': ('com/htmlparser', 'Utility'), 'Kuguo': ('com/kuguo', 'Targeted ads'),
'Mads': ('com/mads', 'Targeted ads'), 'Jcraft': ('com/jcraft', 'Utility'), 'Restlet': ('com/restlet', 'Utility'), 'Ubikod': ('com/ubikod', 'Mobile analytics'),
'Widespace': ('com/widespace', 'Targeted ads'), 'Jakewharton': ('com/jakewharton', 'Ui component'), 'Yicha': ('com/yicha', 'Targeted ads'), 'Casee':
('com/casee', 'Targeted ads'), 'Energysource': ('com/energysource', 'Targeted ads'), 'Wqmobile': ('com/wqmobile', 'Targeted ads'), 'Fortumo': ('com/fortumo', 'Payment'), 'Kuad': ('com/kuad', 'Targeted ads'), 'Skyhookwireless': ('com/skyhookwireless', 'Utility'), 'Adcenix': ('com/adcenix', 'Targeted ads'),
'Wutka': ('com/wutka', 'Utility'), 'Openintents': ('com/openintents', 'Game engine'), 'Winad': ('com/winad', 'Targeted ads'), 'Utilities':
('com/utilities', 'Utility'), 'Mapabc': ('com/mapabc', 'Content provider'), 'Guohead': ('com/guohead', 'Targeted ads'), 'Db4o': ('com/db4o', 'Utility'),
'Ignitevision': ('com/ignitevision', 'Mobile analytics'), 'Osgi': ('com/osgi', 'Utility'), 'Gfan': ('com/gfan', 'Secondary market'), 'Apprupt': ('com/apprupt',
'Targeted ads'), 'Lmmob': ('com/lmmob', 'Targeted ads'), 'Fractalist': ('com/fractalist', 'Targeted ads'), 'Mortbay': ('com/mortbay', 'Utility'),
'Maps': ('com/maps', 'Utility'), 'Moolah': ('com/moolah', 'Targeted ads'), 'Radiumone': ('com/radiumone', 'Targeted ads'), 'Push': ('com/push', 'Utility')
, 'Donson': ('com/donson', 'Targeted ads'), 'Exchange': ('com/exchange', 'Utility'), 'Transpera': ('com/transpera', 'Targeted ads'), 'Andnav':
('com/andnav', 'Content provider'), 'Oneriot': ('com/oneriot', 'Targeted ads'), 'Proguard': ('com/proguard', 'Utility'), 'Mopay': ('com/mopay', 'Payment'), 'Donple': ('com/donple', 'Targeted ads'), 'Viewpagerindicator': ('com/viewpagerindicator', 'Ui component'), 'Stericson': ('com/stericson', 'Utility'),
'Adzhidian': ('com/adzhidian', 'Targeted ads'), 'Simpleframework': ('com/simpleframework', 'Utility'), 'Joelapenna': ('com/joelapenna', 'Social networking service'), 'Quipper': ('com/quipper', 'Content provider'), 'Sellaring': ('com/sellaring', 'Targeted ads'), 'Hamcrest': ('com/hamcrest', 'Utility'
), 'Yuku': ('com/yuku', 'Utility'), 'Thehttpclient': ('com/thehttpclient', 'Utility'), 'Ximad': ('com/ximad', 'Secondary market'), 'Motorola': ('com/motorola', 'Utility'), 'Adpooh': ('com/adpooh', 'Targeted ads'), 'Zongfuscated': ('com/zongfuscated', 'Payment'), 'Intuit': ('com/intuit', 'Payment'),
'Kankan': ('com/kankan', 'Ui component'), 'Jdom': ('com/jdom', 'Utility'), 'Novell': ('com/novell', 'Development aid'), 'Min3d': ('com/min3d', 'Utility'), 'Relaxng': ('com/relaxng', 'Utility'), 'Afzkl': ('com/afzkl', 'Utility'), 'Slf4j': ('com/slf4j', 'Utility'), 'Ocpsoft': ('com/ocpsoft', 'Utility'
), 'J256': ('com/j256', 'Utility'), 'Helllabs': ('com/helllabs', 'Utility'), 'Apwidgets': ('com/apwidgets', 'Utility'), 'Imagezoom': ('com/imagezoom',
 'Utility'), 'Onbarcode': ('com/onbarcode', 'Utility'), 'Joda': ('com/joda', 'Utility'), 'Mobiledatagroup': ('com/mobiledatagroup', 'Content provider'
), 'Jaxen': ('com/jaxen', 'Utility'), 'Tecnick': ('com/tecnick', 'Utility'), 'Kobjects': ('com/kobjects', 'Utility'), 'Achartengine':
('com/achartengine', 'Utility'), 'Lgpl': ('com/lgpl', 'Utility'), 'Appmakr': ('com/appmakr', 'Utility'), 'Spreada': ('com/spreada', 'Mobile analytics'), 'Aspectj':
('com/aspectj', 'Utility'), 'Objenesis': ('com/objenesis', 'Utility'), 'Metalev': ('com/metalev', 'Utility'), 'Yaml': ('com/yaml', 'Utility'), 'Jbox2d':
 ('com/jbox2d', 'Utility'), 'Scoreninja': ('com/scoreninja', 'Social gaming'), 'Jaudiotagger': ('com/jaudiotagger', 'Utility'), 'Libsvg':
 ('com/libsvg', 'Utility'), 'Taptwo': ('com/taptwo', 'Ui component'), 'Easymock': ('com/easymock', 'Ui component'), 'Aerserv': ('com/aerserv', 'Targeted ads'),
 'Fasterxml': ('com/fasterxml', 'Utility'), 'Perk': ('com/perk', 'Analytics'), 'Google Ads': ('com/google/android/gms/ads', 'Targeted ads'),
 'Millenial media': ('com/millennialmedia', 'Targeted ads'), 'MoPub': ('com/mopub', 'Targeted ads'), 'Google Analytics': ('com/google/android/gms/analytics',
 'Mobile analytics'), 'Amazon Insights': ('com/amazon/insights', 'Analytics'), 'Kontagent': ('com/kontagent', 'Analytics'), 'Crashlytics': ('com/crashlytics'
, 'Utilities'), 'OUTFIT7': ('com/outfit7', 'Targeted ads'), 'DOMOB': ('cn/domob', 'Targeted ads'), 'SMARTMAD': ('cn/smartmad', 'Targeted ads'),
'IQzone': ('com/IQzone', 'Targeted ads'), 'AdIQuity': ('com/adiquity', 'Targeted ads'), 'ADITION': ('com/adition', 'Targeted ads'), 'AdMarvel':
('com/admarvel', 'Targeted ads'), 'AdMob': ('com/admob', 'Targeted ads'), 'Receptiv': ('com/receptive', 'Targeted ads'), 'MobFox': ('com/mobfox', 'Targeted ads'),
 'AdsWizz': ('com/adswizz', 'Targeted ads'), 'Appboy': ('com/appboy', 'Targeted ads'), 'AppFlood': ('com/appflood', 'Targeted ads'), 'Applifier':
 ('com/applifier', 'Targeted ads'), 'AppLovin': ('com/applovin', 'Targeted ads'), 'AppNexus': ('com/appnexus', 'Targeted ads'), 'apprupt': ('com/apprupt',
'Targeted ads'), 'Appsflyer': ('com/appsflyer', 'Targeted ads'), 'Bee7': ('com/bee7', 'Targeted ads'), 'bluekai': ('com/bluekai', 'Targeted ads'),
'BrightRoll': ('com/brightroll', 'Targeted ads'), 'Unknown': ('jp/appAdForce', 'Targeted ads'), 'CrossPromotion': ('com/crossPromotion', 'Targeted ads'),
 'DirectTAP': ('com/directtap', 'Targeted ads'), 'FIKSU': ('com/fiksu', 'Targeted ads'), 'FusePowered': ('com/fusepowered', 'Targeted ads'),
 'GrowMobile': ('com/growmobile', 'Targeted ads'), 'heyZap': ('com/heyzap', 'Targeted ads'), 'hyprMX': ('com/hyprmx', 'Targeted ads'), 'ironSource':
 ('com/ironsource', 'Targeted ads'), 'AdColony (Jirbo)': ('com/jirbo', 'Targeted ads'), 'jumptap': ('com/jumptap', 'Targeted ads'), 'Kahuna': ('com/kahuna',
 'Targeted ads'), 'MDOTM': ('com/mdotm', 'Targeted ads'), 'MediaBrix': ('com/mediabrix', 'Targeted ads'), 'mobclix': ('com/mobclix', 'Targeted ads'),
 'mologiq': ('com/mologiq', 'Targeted ads'), 'nanigans': ('com/nanigans', 'Targeted ads'), 'NativeX': ('com/nativex', 'Targeted ads'), 'Pollfish':
 ('com/pollfish', 'Targeted ads'), 'quantcast': ('com/quantcast', 'Targeted ads'), 'RADIUMONE': ('com/radiumone', 'Targeted ads'), 'Smart Ad Server':
 ('com/smartadserver', 'Targeted ads'), 'Fyber': ('com/sponsorpay', 'Targeted ads'), 'StartApp': ('com/startapp', 'Targeted ads'), 'Supersonic':
 ('com/supersonicads', 'Targeted ads'), 'phunware': ('com/tapit', 'Targeted ads'), 'TapJoy': ('com/tapjoy', 'Targeted ads'), 'TAPSENSE': ('com/tapsense', 'Targeted ads'
), 'TREMOR': ('com/tremorvideo', 'Targeted ads'), 'Trialpay': ('com/trialpay', 'Targeted ads'), 'Unity Ads': ('com/unity3d/ads', 'Targeted ads'),
'Urban Ariship': ('com/urbanairship', 'Targeted ads'), 'Vungle': ('com/vungle', 'Targeted ads'), 'Nativex': ('com/w3i', 'Targeted ads'), 'YOC': ('com/yoc'
, 'Targeted ads'), 'YOZIO': ('com/yozio', 'Targeted ads'), 'YuMe': ('com/yume', 'Targeted ads'), 'ZestADZ': ('com/zestadz', 'Targeted ads'),'kiip':
('me/kiip', 'Targeted ads'), 'metaps': ('net/metaps', 'Targeted ads'), 'YouAppi ': ('com/youappi ', 'Targeted ads'), 'LEADBOLT': ('com/leadbolt',
'Targeted ads'), 'FreeWheel': ('com/freewheel', 'Targeted ads'), 'Adxtracking': ('com/AdX', 'Mobile analytics'), 'Ktplay': ('com/ktplay', 'Mobile analytics'),
'mobile app tracking': ('com/mobileapptracker', 'Mobile analytics'), 'adjust': ('com/adjust', 'Mobile analytics'), 'APP DYNAMICS': ('com/appdynamics',
'Mobile analytics'), 'AppFireworks': ('com/appfireworks', 'Mobile analytics'), 'Apptimize': ('com/apptimize', 'Mobile analytics'), 'At Internet':
('com/atinternet', 'Mobile analytics'), 'Kochava': ('com/kochava', 'Mobile analytics'), 'New Relic': ('com/newrelic', 'Mobile analytics'), 'Omniata':
('com/omniata', 'Mobile analytics'), 'Ooyala': ('com/ooyala', 'Mobile analytics'), 'OtherLevels': ('com/otherlevels', 'Mobile analytics'), 'Session m':
('com/sessionm', 'Mobile analytics'), 'Swrve': ('com/swrve', 'Mobile analytics'), 'UPSIGHT': ('com/upsight', 'Mobile analytics'), 'webtrekk':
('com/webtrekk', 'Mobile analytics'), 'webtrends': ('com/webtrends', 'Mobile analytics'), 'INFOnline': ('de/infonline', 'Mobile analytics'), 'PartyTrack':
('it/partytrack', 'Mobile analytics'), 'HOCKETAPP': ('net/hockeyapp', 'Utility'), 'COREMEDIA': ('com/coremedia', 'Utility'), 'FGL': ('com/fgl', 'Utility'),
 'Helpshift': ('com/helpshift', 'Utility'), 'kamcord': ('com/kamcord', 'Utility'), 'Prime31': ('com/prime31', 'Utility'), 'SmartFoxServer':
 ('com/smartfoxserver', 'Utility'), 'Steema': ('com/steema', 'Utility'), 'ThreatMetrix': ('com/threatmetrix', 'Utility'), 'TIM Group': ('com/timgroup', 'Utility'
), 'Truvie': ('com/truvie', 'Utility'), 'Squareup': ('com/squareup', 'Payment'), 'Batch ': ('com/batch ', 'Mobile analytics'), 'Oneaudience ':
 ('com/oneaudience ', 'Mobile analytics'), 'Crystalapp': ('co/crystalapp ', 'Utility::Contentblocker'), 'Tjeannin': ('com/Tjeannin ', 'Utility')}

    return d

def returnSmaliKey(dict, folderList):

    possibleLibrary = []
    alreadyChecked = []
    for item in folderList:

        for name, tuple in dict.items():


            if tuple[0][:-1] in item and name not in possibleLibrary:

                possibleLibrary.append(name)
                alreadyChecked.append(tuple[0][:-1])


    return possibleLibrary


def getSmaliFolders(app_id):
    path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s"%app_id
    list = []

    os.chdir(path)
    dir_list = os.walk('.').__next__()[1]

    for item in dir_list:
        if 'smali' in item:
            list.append(os.path.join(path,item))

    return list


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

def ReceiversFromXML(manifestPATH):
    permissionList = []
    permissionListLevel = []
    root = ET.parse(manifestPATH).getroot()
    application = root.findall("permission")


    for x in application:

        x.find('provider')


    return permissionList

def usesPermissionsFromXML(manifestPATH):

    permissionList = []
    permissionListLevel = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("uses-permission")

    for perm in permissions:
        for att in perm.attrib:
            permissionList.append(perm.attrib[att])


    permissionList.append("android.permission.BIND_CARRIER_SERVICES");
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

    return dictionary

def getPermissionsDictionary():
    dictionary = {'ACCEPT_HANDOVER': 'dangerous', 'ACCESS_BACKGROUND_LOCATION': 'dangerous', 'ACCESS_CALL_AUDIO': 'signature|appop', 'ACCESS_CHECKIN_PROPERTIES': 'N/A',
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
     'QUERY_ALL_PACKAGES': 'N/A', 'READ_CALENDAR': 'dangerous', 'READ_CALL_LOG': 'dangerous', 'READ_CONTACTS': 'dangerous', 'READ_EXTERNAL_STORAGE': 'dangerous',
     'READ_INPUT_STATE': 'N/A', 'READ_LOGS': 'N/A', 'READ_PHONE_NUMBERS': 'dangerous', 'READ_PHONE_STATE': 'dangerous', 'READ_PRECISE_PHONE_STATE': 'N/A',
     'READ_SMS': 'dangerous', 'READ_SYNC_SETTINGS': 'normal', 'READ_SYNC_STATS': 'normal', 'READ_VOICEMAIL': 'signature|privileged', 'REBOOT': 'N/A',
     'RECEIVE_BOOT_COMPLETED': 'normal', 'RECEIVE_MMS': 'dangerous', 'RECEIVE_SMS': 'dangerous', 'RECEIVE_WAP_PUSH': 'dangerous', 'RECORD_AUDIO': 'dangerous',
     'REORDER_TASKS': 'normal', 'REQUEST_COMPANION_RUN_IN_BACKGROUND': 'normal', 'REQUEST_COMPANION_USE_DATA_IN_BACKGROUND': 'normal', 'REQUEST_DELETE_PACKAGES': 'normal',
     'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS': 'normal', 'REQUEST_INSTALL_PACKAGES': 'signature', 'REQUEST_PASSWORD_COMPLEXITY': 'normal', 'RESTART_PACKAGES': 'N/A',
     'SEND_RESPOND_VIA_MESSAGE': 'N/A', 'SEND_SMS': 'dangerous', 'SET_ALARM': 'normal', 'SET_ALWAYS_FINISH': 'N/A', 'SET_ANIMATION_SCALE': 'N/A', 'SET_DEBUG_APP': 'N/A',
     'SET_PREFERRED_APPLICATIONS': 'N/A', 'SET_PROCESS_LIMIT': 'N/A', 'SET_TIME': 'N/A', 'SET_TIME_ZONE': 'N/A', 'SET_WALLPAPER': 'normal', 'SET_WALLPAPER_HINTS': 'normal',
     'SIGNAL_PERSISTENT_PROCESSES': 'N/A', 'SMS_FINANCIAL_TRANSACTIONS': 'signature|appop', 'START_VIEW_PERMISSION_USAGE': 'signature|installer', 'STATUS_BAR': 'N/A',
     'SYSTEM_ALERT_WINDOW': 'signature|preinstalled|appop|pre23|development', 'TRANSMIT_IR': 'normal', 'UNINSTALL_SHORTCUT': 'N/A', 'UPDATE_DEVICE_STATS': 'N/A',
     'USE_BIOMETRIC': 'normal', 'USE_FINGERPRINT': 'normal', 'USE_FULL_SCREEN_INTENT': 'normal', 'USE_SIP':'dangerous', 'VIBRATE': 'normal', 'WAKE_LOCK': 'normal',
     'WRITE_APN_SETTINGS': 'N/A', 'WRITE_CALENDAR': 'dangerous', 'WRITE_CALL_LOG': 'dangerous', 'WRITE_CONTACTS': 'dangerous',
     'WRITE_EXTERNAL_STORAGE': 'dangerous', 'WRITE_GSERVICES': 'N/A', 'WRITE_SECURE_SETTINGS': 'N/A', 'WRITE_SETTINGS': 'signature|preinstalled|appop|pre23',
     'WRITE_SYNC_SETTINGS': 'normal', 'WRITE_VOICEMAIL': 'signature|privileged'}
    return dictionary

def mergeLists(listA, listB):
    result = {}
    for a in listA:
        for b in listB:


            editedString = b.replace(a+" ", "")
            if(a == "Installs"):
                editedString = editedString.replace(",","")
                editedString = editedString.replace("+","")

            if(a == "Installs" and int(editedString) < 1000001):
                editedString = editedString + ", Warning: Low amount of users"

            result[a] = editedString
            listB.remove(b)
            break
    return result


def getDeveloperLinks(soup):

    string = ""
    for test in soup.find_all("div",{"class":"hAyfc"}):
        stringTest = str(test)


        DeveloperWebsite = ""
        DeveloperEmail = ""
        PrivacyPolicy = ""

        if "<div class=\"BgcNfc\">Developer" in stringTest:
            if stringTest.find("hrTbp\" href=") > 1:
                websitePos = stringTest.find(">Visit website")
                QuoteLast = stringTest.rfind('\"',0,websitePos)

                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)

                DeveloperWebsite = stringTest[QuoteSecond+1:QuoteLast]

            if stringTest.find("hrTbp euBY6b\" href=") > 1:
                websitePos = stringTest.find("hrTbp euBY6b\" href=")+27
                endWebPost =stringTest.find('"',websitePos+2)

                DeveloperEmail = stringTest[websitePos:endWebPost]

            if stringTest.find(">Privacy Policy") > 1:
                PrivacyPos = stringTest.find(">Privacy Policy")

                QuoteLast = stringTest.rfind('\"',0,PrivacyPos)

                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)

                PrivacyPolicy = stringTest[QuoteSecond+1:QuoteLast]
                #now i need to find last two substrings before PrivacyPos (" " "), and get the reference there


        links = {"Developer Website":DeveloperWebsite,"Developer Email":DeveloperEmail,"Privacy Policy":PrivacyPolicy}


    return links

def metaFromWebsite(appID):
    URL = "https://play.google.com/store/apps/details?id="+appID+"&hl=en_AU"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    links = getDeveloperLinks(soup)

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


    return Meta

    #with open(File_URL, 'w', encoding='utf-8') as f_out: COMMENTED OUT 31 MARCH 2020
    #    f_out.write(soup.prettify())

def getRSAFile(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.RSA'):
                return str(file)



def makeCertificateFile(appID):
    apkFolder = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads",appID)
    CertFolder = os.path.join(apkFolder,   r"original\META-INF")
    RSAFileName = getRSAFile(CertFolder)
    os.chdir(CertFolder)
    os.system("openssl verify CERT.RSA") #this doesnt do anything, this checks a .pem file

    CertFile = r"original\META-INF\%sCertFile.txt" %(appID)
    apkCertFile = os.path.join(apkFolder, CertFile)
    certificateFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\certificate"


    systemString = "openssl pkcs7 -inform DER -in "+RSAFileName+" -out "+appID+"CertFile.txt  -print_certs -text"
    os.system(systemString)


    shutil.copy(apkCertFile, certificateFolder)



    os.remove(apkCertFile)
    #os.chdir(apkFolder)

def RSAtoPEM(appID):
    apkFolder = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads",appID)
    CertFolder = os.path.join(apkFolder,   r"original\META-INF")
    os.chdir(CertFolder)
    systemString = "openssl pkcs7 -inform DER -in CERT.RSA -out "+appID+"CertFile.pem  -print_certs -text"
    os.system(systemString)




def PemCertificate(appID):
    apkFolder = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads",appID)
    CertFolder = os.path.join(apkFolder,   r"original\META-INF")
    os.chdir(CertFolder)
    try:
        make_pem = "openssl pkcs7 -in CERT.RSA -inform DER -print_certs -out "+ appID+  "cert.pem"
        os.system(make_pem)
    except:
        print("THERE IS AN ERROR IN THIS")

    CertFile = r"original\META-INF\%scert.pem" %(appID)
    apkCertPemFile = os.path.join(apkFolder, CertFile)
    CertPemFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\Cert Pem Files"
    try:
        shutil.copy(apkCertPemFile, CertPemFolder)
        os.remove(apkCertFile)
    except:
        pass

def VerifyCert(appID):
    apkFolder = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads",appID)
    CertFolder = os.path.join(apkFolder,   r"original\META-INF")
    os.chdir(CertFolder)
    os.system("openssl verify CERT.RSA")


def VerifyCertificate(appID):
    #Not working
    apkFolder = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads",appID)
    CertFolder = os.path.join(apkFolder,   r"original\META-INF")
    os.chdir(CertFolder)
    os.system("openssl verify CERT.RSA")


    os.chdir(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\Cert Pem Files")
    os.system("openssl verify "+appID+"cert.pem")

def SaveFiletoDatabase(filePath, typeOfFile, modelInstance, apkCode):
    #typeOfFile can be "Cert", "VT", "Static"
    f = open(filePath,'r')

    if f:
        file_content = ContentFile(f.read())
        print(f.read())
        print(file_content)
        if typeOfFile == "Static":
            modelInstance.jsonFile.save(apkCode+ " Static and Meta.txt",file_content)
        if typeOfFile == "VT":
            modelInstance.VTFile.save(apkCode+ " VirusTotal.txt",file_content)
        if typeOfFile == "CertFile":
            modelInstance.certFile.save(apkCode+ " Certificate.txt",file_content)
        modelInstance.save()
    f.close()
    modelInstance.save()



class APKAnalysis():
    def __init__(self, name="", fileSize="", VTmd5="", VTmsg="", VTpermalink="", VTresource="", VTresponsecode="", VTscanID="",
    VTsha1="", VTsha256="", VTtotal="", VTpositives="",usesPermissions = "", permissions = "", metaData ="", rating="", description="", service=""):
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
        self.VTtotal = VTtotal
        self.VTpositives = VTpositives
        self.usesPermissions = usesPermissions
        self.permissions = permissions
        self.service = service
        self.metaData = metaData
        self.rating = rating
        self.description = description
