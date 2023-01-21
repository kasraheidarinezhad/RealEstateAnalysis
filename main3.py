import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(style="whitegrid", palette="colorblind")

data = pd.read_csv("zillow.csv") 
list = ["Condo for sale", "House for sale"]

filtered_data = data.loc[data['TypeofProperty'].isin(list)]

fig, ax = plt.subplots(figsize=(10,6))
ax = sns.boxplot(x='TypeofProperty', y='Price', data=data, order=["Condo for sale", "House for sale"])
#ax = sns.swarmplot(x="TypeofProperty", y="Price", data=filtered_data, color=".25", order=["Condo for sale", "House for sale"])
ax.set_xlabel('Type')
ax.set_ylabel('Price')
plt.title('Sale by Type',fontsize=16)
labels = [item.get_text() for item in ax.get_xticklabels()]
labels[0] = 'Condo for sale'
labels[1] = 'House for sale'
ax.set_xticklabels(labels)
plt.show()
#plt.savefig('test.png', dpi=300, bbox_inches='tight')