from base import CrawlerBase
from bs4 import BeautifulSoup
import os, csv

baseURL = "https://www.bis.doc.gov/dpl/public/dpl.php"

response = CrawlerBase.getdata(baseURL)

f = open(os.getcwd() + 'data2.csv', 'a', newline='', encoding='utf8')
writer = csv.writer(f)

soup = BeautifulSoup(response.text, 'html.parser') 
table = soup.find_all('table')[0]
data = table.find_all('tr')

for x in data:
    dataappendlist = []
    y = x.find_all('td')
    #y = str(y)
    #y = y.replace('<br/>', '</td><td>')
    #y = BeautifulSoup(y, 'html.parser')
    for z in y:
        dataappendlist.append(z.text)
    print(dataappendlist)
    writer.writerow(dataappendlist)

