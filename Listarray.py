urlList = []
urlList.append("'https://www.zillow.com/homes/for_sale/Vancouver,-BC_rb/'")

for item in range(2,50):
    urlList.append("'https://www.zillow.com/homes/for_sale/Vancouver,-BC_rb/" + str(item)+"_p/'")

print(urlList,"\n")