from tabulate import tabulate
from bs4 import BeautifulSoup, SoupStrainer
import os, csv
import urllib2
import requests
import datetime

headers = ["Tender Group ID", "Main title","Tender ID","Sub Title","Category","Location","Close On Date"]

day = int(datetime.datetime.now().strftime("%d")) - 1
month = datetime.datetime.now().strftime("%B")
year = datetime.datetime.now().strftime("%Y")

def getInfo(url):
    data = []
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    soup.prettify()
    soup = BeautifulSoup(html, "html5lib")
    soup.prettify()
    table = soup.findAll('table')
    # table = soup.findAll('table',attrs={'id': 'tbl'})
    rows = table[0].findAll('tr')       #1st table
    #
    # #Configuring

    for tr in rows:
        cols = tr.findAll('td')
        if cols is not None and len(cols) > 0:
            # cols = [ele.text.strip() for ele in cols]
            # data.append([ele for ele in cols if ele])
            table = [[cols[0].text, cols[1].text,cols[2].text,cols[3].text,cols[4].text,cols[5].text,cols[6].text]]
            print tabulate(table, headers, tablefmt="grid")
            #print cols.text
getInfo("https://www.al-arafahbank.com/e-tender")