import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
from matplotlib import pyplot

df = pd.read_csv('zillow.csv')

fig, (ax1, ax2, ax3) = plt.subplots(1,3)

# Use ax for both
#df[df['TypeofProperty'] == 'Condo for sale'].plot(x='beds', y='Price', ax=ax, label='Condo')
#df[df['TypeofProperty'] == 'House for sale'].plot(x='beds', y='Price', ax=ax, label='House')
#df[df['TypeofProperty'] == 'Multi-family home for sale'].plot(x='beds', y='Price', ax=ax, label='Multi-family home')
#ax.set_title("Property Sale by Type")
#plt.show()
sub_df1 = df[df['TypeofProperty'] == 'Condo for sale']
sub_df2 = df[df['TypeofProperty'] == 'House for sale']
sub_df3 = df[df['TypeofProperty'] == 'Multi-family home for sale']
ax1 = plt.hist(sub_df1['Price'], bins=20, label=['Price', 'Beds'])
ax2 = plt.hist(sub_df2['Price'], bins=20, label=['Price', 'Beds'])
ax3 = plt.hist(sub_df3['Price'], bins=20, label=['Price', 'Beds'])
#bins = np.linspace(100)
#pyplot.hist(sub_df1, 20, alpha=0.5, label='x')
#pyplot.hist(sub_df2, 20, alpha=0.5, label='y')
#pyplot.legend(loc='upper right')
#pyplot.show()
#ax.xaxis.set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x), ',')))

#ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter(['{:,}'.format(int(x))]))

#ax.xaxis.set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x), ',')))
"""
xlabels = ['{:,}'.format(int(x)) + 'K' for x in ax.get_xticks()/1000]
ax[0].set_xticklabels(xlabels)
start, end = ax[0].get_xlim()
ax[0].xaxis.set_ticks(np.arange(0, end, 1000000))
ax[0].xticks(rotation=30)
ax[0].title('Type = Condo')
"""
plt.show()



