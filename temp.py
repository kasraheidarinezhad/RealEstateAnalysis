import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import plotly.express as px
import seaborn as sns
import mplfinance as fplt

# Nominal: the data can only be categorized.  without a natural order or rank. Exp: Hair color, nationality, blood type
# Ordinal: the data can be categorized and ranked. It has a predetermined or natural order. 
#          education level (“high school”,”BS”,”MS”,”PhD”), income level (“less than 50K”, “50K-100K”, “over 100K”), satisfaction rating (“extremely dislike”, “dislike”, “neutral”, “like”, “extremely like”)
     
#numerical_attribute = ['index', 'zpid', 'id', 'imgSrc','Price','beds','best_deal','area','baths']
#nominal_attribute = ['detailUrl','imgSrc', 'address','addressStreet','addressZipcode','latLong','has3DModel','brokerName','TypeofProperty']
#Classified_attrubute = ['beds','baths','TypeofProperty']
#list = ["Condo","Multi-family home","Townhouse", ...]


df1 = pd.read_csv('zillow.csv')

df = df1[['Price', 'TypeofProperty' ]]
df['binned_price'] = pd.cut(df.Price, [1, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000])
#df.groupby('binned_price')['TypeofProperty'].value_counts().plot(kind='bar', stacked=True, ylabel='Frequency', xlabel='Price binned',title='Price group frequency by Type', rot=90, fontsize=9)
df.groupby('binned_price').value_counts().plot(kind='bar', stacked=True, ylabel='Frequency', xlabel='Price binned',title='Price group frequency by Type', rot=90, fontsize=9)
df.drop('Price',axis=1,inplace=True)
df_reshaped = df.pivot_table(index=['binned_price'], columns=['TypeofProperty'], aggfunc=len)
#df_reshaped.plot(kind='bar', stacked=True, ylabel='Frequency', xlabel='Price binned',title='Price group frequency by Type', rot=0, fontsize=9)
#g.plot()
plt.show()
