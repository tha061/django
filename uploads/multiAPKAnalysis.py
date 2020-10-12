from .functions import *






def getResultsInListOLD(apkCode):

    jsonClass = APKAnalysis()
    apkPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", apkCode+".apk")
    zipPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", apkCode+".zip")
    apkFolder = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads"
    policyPATH = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\PrivacyPolicyText", apkCode+".txt")
    apkFolderCD = r"Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownload"
    manifestPath  = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s\AndroidManifest.xml"%apkCode

    os.chdir(apkFolder)
    download_apk(apkCode)
    print("Just finishing downloading APK...."+apkCode)

    resultsList = []

    resultsList.append(apkCode)


    if checkApkDownloaded(apkCode):


        #is_valid() checks if all the variable within 'form' have been declared correctly
        #essentiall, this checks if form's variable 'link_text' contains text

        print("form is not valid")

        print("Check if APK Downloaded")
        VirusTotalResults  = vt_scan(apkCode)

        ###VIRUS TOTAL ###
        #appends important virus total results
        resultsList.append(VirusTotalResults[0])
        resultsList.append(VirusTotalResults[-2])
        resultsList.append(VirusTotalResults[-1])
        try: #calculate ratio of positive to total anti-virus engine scans
            resultsList.append(int((VirusTotalResults[-1])/int((VirusTotalResults[-2]))))
        except:
            resultsList.append("NA")

        ###STATIC ANALYSIS ###
        decompileAPK(apkCode, apkFolder, apkFolderCD)
        if(os.path.exists(manifestPath)):
            theseUsesPermissions = usesPermissionsFromXML(manifestPath) #collects permissions
            thesePermissions = permissionsFromXML(manifestPath) #collections permissions
            serviceList = servicesFromXML(manifestPath) #collects service permissions
        else:
            #If the file can't be found, the JSON file will display the below text
            theseUsesPermissions = "Can't decompile properly"
            thesePermissions ="Can't decompile properly"
            serviceList = "Can't decompile properly"
        try:
            #Will try and connect to the Google Play website to scrape the meta-info database
            #Saves the information in the form of a list
            metaInformation = metaFromWebsite(apkCode)
        except:
            print("Can't connect to android website")
            metaInformation = "Can't connect to android website"

        smaliDirectory = returnSmaliKey(returnSmaliTuplDict(), getLibrariesDirectories(apkCode))

        smaliFiles = getLibrariesSmali(apkCode)

        APKfilesize = file_size(apkPATH)

        privacyPolicyText = getTextFromHTML(metaInformation[3].get("Privacy Policy"))
        if(PPShares3rdParty(privacyPolicyText)):
            print("Privacy Policy Claims to Share your information with 3rd party")
            PPClaims3rdPartySharing = True
        else:
            print("Privacy Policy does not claim to share your info")
            PPClaims3rdPartySharing = False

        print("PPClaims3rdPartySharing: "+str(PPClaims3rdPartySharing))

        print("got privacy policy")
        #print("Privacy policy text............")
        #print(privacyPolicyText)
        privacyFile = open(policyPATH, "w")

        try:
            print("in try block")
            privacyFile.write(privacyPolicyText)
            print("try block worked")
        except Exception as e:
            print("exception: ")
            print(e)

            print("Couldn't get the url for privacy policy")
        privacyFile.close()

        jsonClass.name = apkCode
        jsonClass.fileSize = APKfilesize
        jsonClass.VTpermalink = VirusTotalResults[0]
        jsonClass.VTsha1 = VirusTotalResults[1]
        jsonClass.VTresource = VirusTotalResults[2]
        jsonClass.VTresponsecode = VirusTotalResults[3]
        jsonClass.VTscanID  = VirusTotalResults[4]
        jsonClass.VTmsg  = VirusTotalResults[5]
        jsonClass.VTsha256 = VirusTotalResults[6]
        jsonClass.VTmd5 = VirusTotalResults[7]
        jsonClass.VTtotal = VirusTotalResults[8]
        jsonClass.VTpositives = VirusTotalResults[9]
        jsonClass.permissions = thesePermissions
        jsonClass.usesPermissions = theseUsesPermissions
        jsonClass.service = serviceList
        jsonClass.metaData = metaInformation[0]
        jsonClass.rating = metaInformation[1]
        jsonClass.description = metaInformation[2]
        jsonClass.links = metaInformation[3]
        jsonClass.smali_Directories = smaliDirectory
        jsonClass.privacyText = metaInformation[3].get("Privacy Policy")
        serialJSON = jsonClass.__dict__


        jsonPath = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\jsonFolder", apkCode+"JSONFile.txt")
        VirusTotalPath = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\VirusTotal", apkCode+"VirusTotal.txt")
        CertPath = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\certificate", apkCode+"CertFile.txt")

        jsonFile = open(jsonPath, "w")
        json.dump(serialJSON, jsonFile, indent = 2)
        jsonFile.close()

        print("FORM IS VALID")
        if(os.path.exists(manifestPath)):
            makeCertificateFile(apkCode)
        else:
            print("NO CERT FILE")

        instance = Link()
        instance.link_text = apkCode
        SaveFiletoDatabase(jsonPath, "Static", instance, apkCode)
        SaveFiletoDatabase(VirusTotalPath, "VT", instance, apkCode)
        SaveFiletoDatabase(CertPath, "CertFile", instance, apkCode)



    return listToStringCSV(resultsList)
