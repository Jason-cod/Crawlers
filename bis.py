from base import CrawlerBase
from bs4 import BeautifulSoup
import os, csv

writer = CrawlerBase.csvWriter()

baseURL = "https://www.bis.doc.gov/dpl/public/dpl.php"
response = CrawlerBase.getdata(baseURL)
response = response.text.replace('<br />', '</td><td>')

soup = BeautifulSoup(response, 'html.parser')
table = soup.find_all('table')[0]
rows = table.find_all('tr')

for row in rows:
    dataappendlist = []
    cols = row.find_all('td')
    for col in cols:
        dataappendlist.append(col.text)
    writer.writerow(dataappendlist)
