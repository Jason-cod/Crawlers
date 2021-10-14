from base import CrawlerBase
from bs4 import BeautifulSoup
import os
import csv, json

writer = CrawlerBase.csvWriter()
apikey = "z9duUaFUiEUYSHs97CU38fcZO7ipOPvm"

baseURL = "https://apigwext.worldbank.org/dvsvc/v1.0/json/APPLICATION/ADOBE_EXPRNCE_MGR/FIRM/SANCTIONED_FIRM"
response = CrawlerBase.getdata(baseURL, {'apikey': apikey}).json()
 



print(len(response['response']['ZPROCSUPP']))
for count in range(len(response['response']['ZPROCSUPP'])):
    writer.writerow([(response['response']['ZPROCSUPP'][count]["MANDT"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_ID"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_NAME"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_TYPE_CODE"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_PRE_ACRN"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_POST_ACRN"]),
                 (response['response']['ZPROCSUPP'][count]["LAND1"]),
                 (response['response']['ZPROCSUPP'][count]["COUNTRY_NAME"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_STATE_CODE"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_CITY"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_ADDR"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_ZIP_CODE"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_POST_CODE"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_PROV_NAME"]),
                 (response['response']['ZPROCSUPP'][count]["LEGACY_FLG"]),
                 (response['response']['ZPROCSUPP'][count]["UN_SUPP_FLG"]),
                 (response['response']['ZPROCSUPP'][count]["INELIG_FLG"]),
                 (response['response']['ZPROCSUPP'][count]["DEBAR_TYPE"]),
                 (response['response']['ZPROCSUPP'][count]["DEBAR_FROM_DATE"]),
                 (response['response']['ZPROCSUPP'][count]["DEBAR_TO_DATE"]),
                 (response['response']['ZPROCSUPP'][count]["DEBAR_REASON"]),
                 (response['response']['ZPROCSUPP'][count]["AML_ENTR_IND"]),
                 (response['response']['ZPROCSUPP'][count]["ADD_SUPP_INFO"]),
                 (response['response']['ZPROCSUPP'][count]["DNB_ID"]),
                 (response['response']['ZPROCSUPP'][count]["DNB_PAR_ID"]),
                 (response['response']['ZPROCSUPP'][count]["DNB_ULTM_ID"]),
                 (response['response']['ZPROCSUPP'][count]["CRIS_SUPP_ID"]),
                 (response['response']['ZPROCSUPP'][count]["SUPP_ELIG_STAT"]),
                 (response['response']['ZPROCSUPP'][count]["CRPD_MATCH"]),
                 (response['response']['ZPROCSUPP'][count]["CRPD_STAT"]),
                 (response['response']['ZPROCSUPP'][count]["ELIG_STAT"]),
                 (response['response']['ZPROCSUPP'][count]["CREATE_USER"]),
                 (response['response']['ZPROCSUPP'][count]["CREATE_DATE"]),
                 (response['response']['ZPROCSUPP'][count]["CREATE_TIME"]),
                 (response['response']['ZPROCSUPP'][count]["UPD_USER"]),
                 (response['response']['ZPROCSUPP'][count]["UPD_DATE"]),
                 (response['response']['ZPROCSUPP'][count]["UPD_TIME"]),
                 (response['response']['ZPROCSUPP'][count]["REGISTER"]),
                 (response['response']['ZPROCSUPP'][count]["REGISTER_ID"]),
                 (response['response']['ZPROCSUPP'][count]["PARENT"]),
                 (response['response']['ZPROCSUPP'][count]["CREATE_USER_NAME"]),
                 (response['response']['ZPROCSUPP'][count]["UPD_USER_NAME"]),
                 (response['response']['ZPROCSUPP'][count]["RECHK_IND"]),
                 (response['response']['ZPROCSUPP'][count]["INELIGIBLY_STATUS"]),
                 (response['response']['ZPROCSUPP'][count]["LAST_REFRESH_DATE"])
                ])
    
