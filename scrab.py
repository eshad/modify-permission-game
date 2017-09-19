from bs4 import BeautifulSoup, SoupStrainer
import os, csv
import urllib2
import requests
import datetime

day = int(datetime.datetime.now().strftime("%d")) - 1
month = datetime.datetime.now().strftime("%B")
year = datetime.datetime.now().strftime("%Y")

#fileLinks = open("links.csv","w")
#file_details = open("details.csv","w")



#links = []
file_details = open("details.txt", "a")

def searchUrl(url):
    #Searching links
    return getInfo(url)

def getInfo(str):
    from details import main as mn
    details = mn(str)
    #file_details.write(str(details))
    return details

def findLinks(lnks):
    # url = "http://epzbangladesh.org.bd/investors/investor_report/dhaka-export-processing-zone-2"
    url = lnks
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    soup.prettify()
    table = soup.find('table', attrs={'id': 'tbl'})
    rows = table.findAll('tr')
    searchUrlDetails = []
    for tr in rows:
        cols = tr.findAll('td')
        if cols is not None and len(cols) > 0:
            #print cols[0]
            #links = cols[0].find('a').get('href')
            data = cols[0].find('a').get('href')
            #links.append(data[1:])
            #print "http://www.bkmea.com/member" + data[1:]
            #with file_details as myfile:
            fileData = searchUrl("http://www.bkmea.com/member" + data[1:])
            searchUrlDetails.append(str(fileData))
                #myfile.write(str(fileData))
            #fileLinks.write(str(links))
    file_details.write(str(searchUrlDetails))
    file_details.write("\n")

def countLinkd():
    a = 0
    while(a <=25):      # a to z page

        alpha = chr(ord('a') + a)
        url = "http://www.bkmea.com/member/index.php?Index=" + alpha
        findLinks(url)
        print "Done: " + url
        from getPage import pagination as pg
        details = pg(url)
        for i in details[0]:
            findLinks("http://www.bkmea.com/member/" + i)
            print "Done: " + i
        a += 1
countLinkd()
#fileLinks.close()
file_details.close()



