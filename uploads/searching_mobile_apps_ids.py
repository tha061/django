# sudo pip install urllib2
import urllib

# Install bs4

# sudo pip install bs4
from bs4 import BeautifulSoup


# Seed App-IDs

def defineURL(str):
    start_links = [str]
    urls = set(start_links)
    print(urls)
    #findId(urls)

def findId(source):
    ids = []
    soup =  BeautifulSoup(source, "html.parser")
    divs = soup.findAll('div', {'class':'b8cIId ReQCgd Q9MA7b'})
    ids_r =  []
    for item in divs:
        try:
            ids_r.append(item.find('a').attrs['href'].split('id=')[-1])
        except:
            pass
    print("REEEEE")
    print(ids_r)
    print("REEEEEEE SOME MORE")
    return ids_r

def get_source(url):
    request = urllib2.Request('https://play.google.com/store/apps/details?id='+url) #urllib2.urlopen(url)
    page_source =urllib2.urlopen(request).read()
    return page_source

'''
def search(source, depth):
    if depth==1:
        return
    #print source, depth

    try:
        page_source = get_source(source)
        #print page_source
        links = Set(findId(page_source))
    except:
        #print 'some error encountered'
        return

    global urls
    for link in links:
        if link not in urls:
            urls = urls|Set([link])

    for link in urls:
        search(link,depth+1)

count = 0
for start_link in start_links:
    print ("%s : Total apps : %s " % (count, len(urls)))
    search(start_link,0)
    count += 1

fo = open("../data/gcrawler_output.txt", "wb")
for item in urls:
    fo.write("%s\n"%item)
fo.close()
'''
