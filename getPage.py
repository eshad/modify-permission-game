from bs4 import BeautifulSoup, SoupStrainer
import os, csv
import urllib2
import requests
import datetime

# url = "http://epzbangladesh.org.bd/investors/investor_report/dhaka-export-processing-zone-2"
def pagination(url):
    dat = []
    pagination = []
    #url = "http://localhost/members.html"
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    soup.prettify()
    table = soup.find('table', attrs={'id': 'tbl'})
    rows = table.findAll('tr')


    for tr in rows:
        cols = tr.findAll('td')
        if cols is not None and len(cols) > 0:
            #print cols[0]
            #links = cols[0].find('a').get('href')
            data = cols[0].find('div', attrs={'id': 'pagination'})
            if data != None:
                a = data.findAll('a')
                for every in a:
                    pagination.append(every.get('href'))
                page = pagination[:-1]
                dat.append(page)
                dat.append(len(page))       #remove last letter
                return dat


#print pagination("http://localhost/members.html")
