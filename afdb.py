from base import CrawlerBase
from bs4 import BeautifulSoup
import os, csv

writer = CrawlerBase.csvWriter()

baseURL = "https://www.afdb.org/en/projects-operations/debarment-and-sanctions-procedures"
response = CrawlerBase.getdata(baseURL)
response = response.text.replace('<br />', '</td><td>')

soup = BeautifulSoup(response, 'html.parser')
table = soup.find('table', attrs={'id': 'datatable-1'})

#datatable-1
rows = table.find_all('tr')

for row in rows:
    dataappendlist = []
    cols = row.find_all('td')
    for col in cols:
        val = col.text.lstrip().rstrip() 
        dataappendlist.append(val)
    writer.writerow(dataappendlist)
