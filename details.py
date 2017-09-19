from bs4 import BeautifulSoup, SoupStrainer
import os, csv
import requests
import urllib2
import datetime

# file_details = open("details.txt", "a")
#file_details = open("details.csv","w")
def main(lnk):
    return getInfo(lnk)

def getInfo(url):
    data = []
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    soup.prettify()
    soup = BeautifulSoup(html, "html5lib")
    soup.prettify()
    table = soup.findAll('table')
    # table = soup.findAll('table',attrs={'id': 'tbl'})
    rows = table[0].findAll('tr')
    #
    # #Configuring

    for tr in rows:
        cols = tr.findAll('td')
        if cols is not None and len(cols) > 0:
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
    return data
#
# if __name__ == "__main__":
#     main()
#print main("http://localhost/member.html")
#
# file_details.write(str(pagination("http://www.bkmea.com/member/member_details.php?BackView&Page=1&Index=x&MID=1248")))
# print "Done"
# file_details.write(str(main("http://www.bkmea.com/member/member_details.php?BackView&Page=1&Index=x&MID=859")))
# file_details.close()
