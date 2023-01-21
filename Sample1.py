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

data_stat = pd.read_sql(''' SELECT zpid, TypeofProperty, Price, beds, addressStreet, area
                                     FROM VancouverPropertiesTable
                                     WHERE addressStreet LIKE '%Kingsway%'
                                     ORDER BY Price DESC ''', db_conn)
print(data_stat)

engineering_tot = pd.read_sql(''' SELECT SUM(n_enrolled) AS total_engineering_enrollment, COUNT(title) AS total_courses, AVG(price) AS avg_course_purchase, MIN(price) AS min_course_purchase, MAX(price) AS max_course_purchase
                               FROM edx_course_descriptions
                               WHERE subject == 'Engineering'
                               ORDER BY price DESC ''', edx_conn)

data_stat_Avg = pd.read_sql(''' SELECT AVG(Price)AS Avg_price_condo , TypeofProperty, AVG(area) AS Avg_area
                                     FROM VancouverPropertiesTable
                                     WHERE TypeofProperty == 'Condo'  ''', db_conn)
"""
reviews_lec = pd.read_sql(''' SELECT course_title, subject, num_lectures, num_reviews
                             FROM udemy_updated
                             ORDER BY num_reviews DESC''', udemy_conn)
reviews_lec
sns.barplot(x = 'num_reviews', y = 'course_title', data = by_reviews, color = 'red', edgecolor = 'black', ci=False)


print(data_stat_Avg)
