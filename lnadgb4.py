from base import CrawlerBase
from bs4 import BeautifulSoup
import os
import csv

writer = CrawlerBase.csvWriter()

def buildURL(start):
    return "https://lnadbg4.adb.org/oga0009p.nsf/sancALL1P?OpenView&Start="+str(start)+"&Count=999"

def requiredURLs():
    urllist = []
    for x in range(0, 10000, 1000):
        if x==0:
            response = CrawlerBase.getdata(buildURL(1))
            urllist.append(buildURL(1))
        else:
            response=CrawlerBase.getdata(buildURL(x))
            if 'No documents found' in response.text:
                break
            else:
                urllist.append(buildURL(x))
    return(urllist)            

for URL in requiredURLs():
    response = CrawlerBase.getdata(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')[1]
    rows = table.find_all('tr')

    for row in rows:
        dataappendlist = []
        cols = row.find_all('td')
        for col in cols:
            val = col.text.lstrip().rstrip()
            dataappendlist.append(val)
        writer.writerow(dataappendlist)
                
