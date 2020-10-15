import requests, os, json, time


def vt_scan(app_id):
    #this will search on virustotal by the Sha256 of the .apk file, I will need to figure out a way so that if the sha256
    #doesnt work because nobody has uploaded that .apk to VT before, then it uploads the file to VT
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': '40452be02c007065db644040f4ac471a8feca7cdc1db8f46ec6e4003ef531da0'}

    filename = "/home/comp4093/Documents/%s.apk" % app_id
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
    
    jsonPath = os.path.join("/home/comp4093/Documents/", app_id+".txt")
    jsonFile = open(jsonPath, "w")
    json.dump(response.json(), jsonFile)

    return 1

app_ids = [x.strip().replace("\n", "") for x in open('/home/comp4093/Documents/test.txt').readlines()]
#print(app_ids)
#app_hashes = [x.strip().replace("\n", "") for x in open('/home/comp4093/Documents/hash.txt').readlines()]
#print(app_hashes)

count = 0
for app_id in app_ids:
    print(count)
    print(app_id)
    vt_scan(app_id)
    #time.sleep(15)
    count = count + 1