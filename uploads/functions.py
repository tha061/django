from zipfile import ZipFile
import xml.etree.ElementTree as ET



def returnZ(str):
    return str[0]

def permissionsFromXML(manifestPATH):
    permissionList = []
    root = ET.parse(manifestPATH).getroot()
    permissions = root.findall("uses-permission")

    for perm in permissions:
        for att in perm.attrib:
            permissionList.append(perm.attrib[att])
            #print("{}\t:\t{}\n".format(att, perm.attrib[att]))
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


class APKAnalysis():
    def __init__(self, name="", fileSize="", VTmd5="", VTmsg="", VTpermalink="", VTresource="", VTresponsecode="", VTscanID="", VTsha1="", VTsha256="", permissions = ""):
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
        self.permissions = permissions
