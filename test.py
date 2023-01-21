import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import plotly.express as px
import seaborn as sns


"""
def main1():
    propertyListFrame = pd.read_csv('zillow.csv')
    plt.figure(figsize = (6,6))
    sns.countplot(x="beds", data= propertyListFrame.loc[propertyListFrame['beds']<=20]).set_title('Houses with less than SEVEN bedrooms')
    plt.show() 

def main3():
    plt.figure(figsize = (6,6))
    plt.xlim(1880, 2016)
    sns.distplot(propertyListFrame['unformattedPrice'], kde=False, color='red')
    plt.show()
"""
def Histogram1():    # histogram of target variable = Price
    sns.set_theme()
    graph = sns.displot(data=propertyListFrame, x="Price", kde=True, kind='hist', log_scale=True, bins=50)
    graph.set(title="Histogram of Sale Price")
    for ax in graph.axes.flat:
       ax.xaxis.set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.xticks(rotation=30)
    plt.show()
    
def fun():    # Shape of Data and 4 Major Statis Factor
    print(f"Number of samples: {propertyListFrame.shape[0]}")
    print(f"Number of features in set: {propertyListFrame.shape[1]}")
    print("Features:")
    print(propertyListFrame.columns.values)
    Mean = propertyListFrame["Price"].mean()
    Median = propertyListFrame["Price"].median()
    Skewness = propertyListFrame["Price"].skew()
    Kurtosis =propertyListFrame["Price"].kurtosis()
    print(f"Mean: {Mean:,.2f}")
    print(f"Median: {Median:,.2f}")
    print(f"Skewness: {Skewness:.4f}")
    print(f"Kurtosis: {Kurtosis:.4f}")

def Histogram2():    # histogram of target variable=price based on 4 factor
    sns.set_theme()
    graph = sns.displot(data=propertyListFrame, x="Price", kde=True, kind='hist', log_scale=True, bins=50)
    graph.set(title="Histogram of Sale Price")
    for ax in graph.axes.flat:
       ax.xaxis.set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.xticks(rotation=30)
    plt.show()

def Histogram3():   # Histogram top 20 Realtor
    df['brokerName'] = df['brokerName'].str.strip()
    #print(df['brokerName'].nunique())   #print number of brokers
    graph = df['brokerName'].value_counts()[:20]
    graph.plot(kind='barh', fontsize=10, title="Top 20 listing-creator realtor")
    plt.show()


def main():
    Histogram2()

if __name__ == "__main__":
    propertyListFrame = pd.read_csv('zillow.csv')
    main()