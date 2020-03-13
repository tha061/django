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

def usesPermissionsFromXML(manifestPATH):
    permissionList = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("uses-permission")

    for perm in permissions:
        for att in perm.attrib:
            permissionList.append(perm.attrib[att])
            #print("{}\t:\t{}\n".format(att, perm.attrib[att]))
    return permissionList

def permissionsFromXML(manifestPATH):
    permissionList = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("permission")

    for perm in permissions:
        print("new perm: ")
        concat = ""
        for att in perm.attrib:

            #position = att.rfind("}")
            splitAtt = att.split("}")
            cleanAtt = splitAtt[1]

            concat = concat + "   "+ cleanAtt + ": " +perm.attrib[att]
            #print("{}\t:\t{}\n".format(att, perm.attrib[att]))
        print("final concat")
        print(concat)
        permissionList.append(concat)
    return permissionList

def servicesFromXML(manifestPATH):
    print("In services from XML function")
    permissionList = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("service")

    for perm in permissions:
        print("new perm: ")
        concat = ""
        for att in perm.attrib:

            #position = att.rfind("}")
            splitAtt = att.split("}")
            cleanAtt = splitAtt[1]

            concat = concat + "   "+ cleanAtt + ": " +perm.attrib[att]
            #print("{}\t:\t{}\n".format(att, perm.attrib[att]))
        print("final concat")
        print(concat)
        permissionList.append(concat)
    return permissionList

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
        print(listOfFileNames)
        print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

        zipObj.extract("AndroidManifest.xml", r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads")
   # Iterate over the file names
        #for fileName in listOfFileNames:
       # Check filename endswith csv
            #if fileName.endswith('.xml'):
           # Extract a single file from zip
                #zipObj.extract(fileName, 'temp_csv')

def metaFromWebsite(appID):
    URL = "https://play.google.com/store/apps/details?id="+appID+"&hl=en_AU"
    page = requests.get(URL)
    #print("PAGE")
    #print(page.text)
    soup = BeautifulSoup(page.content, 'html.parser')
    #soup.prettify()
    #File_URL = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\webText\web.txt"
    #File_object = open(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\webText\web.txt","wb")
    #print(soup)
    #test = soup.find('div',attrs={"class":"hAyfc"})
    #print(test)
    result = [e.get_text(separator=" ").strip() for e in soup.find_all("div",{"class":"hAyfc"})]
    rating = soup.find("div",{"class":"BHMmbe"}).get_text(separator=" ").strip()
    description = soup.find("div",{"class":"DWPxHb"}).get_text(separator=" ").strip()

    Meta = []

    Meta.append(result)
    Meta.append(rating)
    Meta.append(description)

    return Meta
    #print(result)
    #print(rating)
    #print(description)
    #print("SPACES")


    #File_object.write(str(soup.html.encode('utf8')))

    with open(File_URL, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())
    #File_object.write(page.text.encode('utf-8'))
    #test = soup.xpath("//div[@itemprop='numDownloads']/text()").extract_first().strip()
    #print("SOUP")
    #print(soup)
    #results = soup.find(id='htlgb')
    print("REEEESSSSSSSSSULLLLTTSS")
    #print(results)

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
