from datetime import datetime, timedelta
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd


sector = input("""Choose from the following sectors -
                    Basic Industries
                    Capital Goods
                    Consumer Durables
                    Consumer Non-Durables
                    Consumer Services
                    Energy
                    Finance
                    Health Care
                    Miscellaneous
                    Public Utilities
                    Technology
                    Transportation
                    \n""")

startDate = datetime.today() - timedelta(days=2)
endDate = datetime.today()
yf.pdr_override()
totalStocks = pd.read_csv('Stock List.csv')
choiceStocks = totalStocks[totalStocks["Sector"] == sector]
stockList = choiceStocks.Symbol


#Declares variable to store stocks that fit the requirements
global weeklyPlays
weeklyPlays = []

#Iterate through stocks to find inside bars
def screener():
    for i in stockList:
       data = pdr.get_data_yahoo(i, start=startDate, end=endDate)
       currentDate = data.index
       highPrice = data['High']
       lowPrice = data['Low']
       for j in range(len(data)-1):
           if highPrice[j] >= highPrice[j+1] and lowPrice[j] <= lowPrice[j+1]:
               weeklyPlays.append(i)

if __name__ == "__main__":
    screener()

print("Here is the list of stocks in the {} sector that had inside bars over the last few days. Multiple entries indicate multiple inside bars.\n".format(sector) + str(weeklyPlays))
