import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.ticker as tkr
import sqlite3

properties = pd.read_csv("zillow.csv")
"""
df['TypeofProperty'] = df['TypeofProperty'].str.strip()
graph = df['TypeofProperty'].value_counts()
graph.plot(kind='bar', fontsize=14, title="Number of Properties Per Category", rot=0)
plt.show()
"""
#print(f"Number of samples: {df.shape[0]}")
#print(f"Number of features in set: {df.shape[1]}")
#print("Features:")
#print(df.dtypes)


Path('VancouverProperties.db').touch()
db_conn = sqlite3.connect('VancouverProperties.db')
db_cursor = db_conn.cursor()
"""
properties.to_sql('VancouverPropertiesTable', db_conn, if_exists='append', index=False)
db_vancouverproperties_init_query = pd.read_sql(''' SELECT * FROM VancouverPropertiesTable ''', db_conn)
db_vancouverproperties_init_query

data_stat = pd.read_sql(''' SELECT zpid, TypeofProperty, Price, beds, addressStreet, area
                                     FROM VancouverPropertiesTable
                                     WHERE addressStreet LIKE '%Kingsway%'
                                     ORDER BY Price DESC ''', db_conn)



data_stat_Avg = pd.read_sql(''' SELECT AVG(Price)AS Avg_price_condo , TypeofProperty, AVG(area) AS Avg_area
                                     FROM VancouverPropertiesTable
                                     WHERE TypeofProperty == 'Condo'  ''', db_conn)
"""

data_set = pd.read_sql(''' SELECT zpid, TypeofProperty, Price, beds, addressStreet, area
                                     FROM VancouverPropertiesTable
                                     WHERE addressStreet LIKE '%Kingsway%'
                                     ORDER BY Price DESC ''', db_conn)
#print(data_stat)
#sns.barplot(x = 'area', y = 'Price', data = data_set, color = 'red', edgecolor = 'black', errorbar=('ci', False))
"""
properties.plot.scatter(x="Price",y="area", title='Relationships between Price and Area', c="beds", cmap='summer')
plt.colorbar(label="Number of Beds")
current_values = plt.gca().get_xticks()
plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in current_values])
"""

plt.rcParams.update( {'figure.figsize':(10,8), 'figure.dpi':100})
plt.scatter(x=properties.Price, y=properties.area, c=properties.beds, cmap='Spectral')
plt.colorbar(label="Number of Beds")
plt.title('Relationships between Price and Area')
plt.xlabel('Price (CA$)')
plt.ylabel('Property Area (Square feet)')
current_values = plt.gca().get_xticks()
plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in current_values])
plt.show()

#print(data_stat_Avg)
