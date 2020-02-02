# sudo pip install urllib2
# not implemented yet
import urllib.request as urllib

# Install bs4

# sudo pip install bs4
from bs4 import BeautifulSoup


# Seed App-IDs

test = []

def defineURL(str):

    #findId(get_source(str))
    search(get_source(str), 2)

def findId(source):
    print("do we get here")
    soup =  BeautifulSoup(source, "html.parser")
    divs = soup.findAll('div', {'class':'b8cIId ReQCgd Q9MA7b'})
    ids_r =  []
    for item in divs:
        print(item)
        try:
            ids_r.append(item.find('a').attrs['href'].split('id=')[-1])
        except:
            pass
    print("REEEEE")
    print(ids_r)
    print("REEEEEEE SOME MORE")
    test = ids_r
    return ids_r

def get_source(url):
    request = urllib.Request('https://play.google.com/store/apps/details?id='+url) #urllib2.urlopen(url)
    page_source = urllib.urlopen(request).read()
    return page_source


def search(source, depth):
    if depth==1:
        return
    #print source, depth

    try:
        page_source = get_source(source)
        #print page_source
        link = findId(page_source)
    except:
        #print 'some error encountered'
        return

    global urls
    if link not in urls:
        urls = urls|Set([link])

    for link in urls:
        search(link,depth+1)

fo = open("..gcrawler_output.txt", "wb")
'''
print("it stops here 1")
for item in test:
    sharedUrl = item
    print("it stops here")
    print("shared urlllll:    "+sharedUrl)
    fo.write(sharedUrl.encode('utf-8'))
'''
fo.close()
