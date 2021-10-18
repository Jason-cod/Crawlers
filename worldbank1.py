from base import CrawlerBase
from bs4 import BeautifulSoup
import os
import csv, json

writer = CrawlerBase.csvWriter()
apikey = "z9duUaFUiEUYSHs97CU38fcZO7ipOPvm"

baseURL = "https://apigwext.worldbank.org/dvsvc/v1.0/json/APPLICATION/ADOBE_EXPRNCE_MGR/FIRM/SANCTIONED_FIRM"
response = CrawlerBase.getdata(baseURL, {'apikey': apikey}).json()

for count in range(len(response['response']['ZPROCSUPP'])):
    record = response['response']['ZPROCSUPP'][count]
    all_data = []
    
    for data in record.keys():
        all_data.append(record[data])   
    
    writer.writerow(all_data)
    
