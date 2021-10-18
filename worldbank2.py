from base import CrawlerBase
from bs4 import BeautifulSoup
import os
import csv

writer = CrawlerBase.csvWriter()

baseURL = "https://www.worldbank.org/en/projects-operations/procurement/debarred-firms"
response = CrawlerBase.getdata(baseURL)

soup = BeautifulSoup(response, 'html.parser')
table = soup.find('table', attrs={'border': '1'})

rows = table.find_all('tr')

for row in rows:
    dataappendlist = []
    cols = row.find_all('td')
    for col in cols:
        val = col.text.lstrip().rstrip()
        dataappendlist.append(val)
    writer.writerow(dataappendlist)
