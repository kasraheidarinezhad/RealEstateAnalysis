import requests
import re
import json
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

city = 'Vancouver,-BC_rb/' #*****change this city to what you want!!!!*****


#feel free to make this prettier

#add headers in case you use chromedriver (captchas are no fun); namely used for chromedriver
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

with requests.Session() as s:
    data_list = []
    resp = s.get('https://www.zillow.com/homes/for_sale/Vancouver,-BC_rb/', headers=req_headers)
    data = json.loads(re.search(r'!--(\{"queryState".*?)-->', resp.text).group(1))
    data_list.append(data)

    for pages in range(1,20):   #just grabbing the first 20 pages
       resp = s.get('https://www.zillow.com/homes/for_sale/Vancouver,-BC_rb/'+str(pages+1)+'_p/', headers=req_headers)
       data = json.loads(re.search(r'!--(\{"queryState".*?)-->', resp.text).group(1))
       data_list.append(data)


df = pd.DataFrame()

def make_frame(frame):
    for i in data_list:
        for item in i['cat1']['searchResults']['listResults']:
            frame = frame.append(item, ignore_index=True)
    return frame

df = make_frame(df)
    
#drop cols
df = df.drop('hdpData', 1) 

#drop dupes
df = df.drop_duplicates(subset='zpid', keep="last")

#filters
df['zestimate'] = df['zestimate'].fillna(0)
df['best_deal'] = df['unformattedPrice'] - df['zestimate']
df = df.sort_values(by='best_deal',ascending=True)

#print('shape:', df.shape)
#print(df[['id','address','beds','baths','area','price','zestimate','best_deal']].head(90))
df.to_csv('zillow3.csv', encoding='utf-8')