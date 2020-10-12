import requests, os, json, time


def vt_scan(app_id):
    #this will search on virustotal by the Sha256 of the .apk file, I will need to figure out a way so that if the sha256
    #doesnt work because nobody has uploaded that .apk to VT before, then it uploads the file to VT
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': '1162652624083e2616b2200d64c68d4ae92722b952c88418d46e46c14383ccae'}

    #filename = os.path.join("C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads", app_id+".apk")
   
    filename = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\apkDownloads\%s.apk" % app_id
    files = {'file': ('%s' % app_id, open(filename, 'rb'))}

    response = requests.post(url, files=files, params=params)
    #js = response.json()

    print(response)

    #jsonPath = os.path.join("/home/comp4093/Documents/virus_total_report", app_id+".txt")

    #with open("/home/comp4093/Documents/virus_total_report/a.txt", "r+") as jsonFile:
    #    data = json.load(jsonFile)
    #    data.update(js)
    #    jsonFile.seek(0)
    #   json.dump(data, jsonFile)
    
    jsonPath = os.path.join(r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\VTHannes", app_id+".txt")
    jsonFile = open(jsonPath, "w")
    json.dump(response.json(), jsonFile)

    return 1

#app_ids = [x.strip().replace("\n", "") for x in open('/home/comp4093/Documents/suspicious_apps.txt').readlines()]
#print(app_ids)
#app_hashes = [x.strip().replace("\n", "") for x in open('/home/comp4093/Documents/hash.txt').readlines()]
#print(app_hashes)


app_id = 'com.nexample.martinmazanec.foamrollercoachapp'
print(app_id)
vt_scan(app_id)

