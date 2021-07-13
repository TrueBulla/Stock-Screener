from datetime import datetime, timedelta
import yfinance as yf #Requires yfinance-0.1.63
from pandas_datareader import data as pdr
import pandas as pd

#Iterate through stocks to find inside bars
def screener():
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

    startDate = datetime.today() - timedelta(days=1)
    endDate = datetime.today()
    weeklyPlays = []
    yf.pdr_override()
    nyseStocks = pd.read_csv('NYSE Stock List.csv')
    nasdaqStocks = pd.read_csv('Nasdaq Stock List.csv')
    bothExchanges = [nyseStocks, nasdaqStocks]
    concExchanges = pd.concat(bothExchanges)
    choiceStocks = concExchanges[concExchanges["Sector"] == sector]
    stockList = choiceStocks.Symbol
    while True:
        try:
            for i in stockList:
                print("Checking price history of {}".format(i))
                data = pdr.get_data_yahoo(i, start=startDate, end=endDate)
                highPrice = data['High']
                lowPrice = data['Low']
                for j in range(len(data)-1):
                    if highPrice[j] >= highPrice[j+1] and lowPrice[j] <= lowPrice[j+1]:
                       weeklyPlays.append(i)

            print("Here is the list of stocks in the {} sector that had inside bars over the last two days.\n".format(sector) + str(weeklyPlays))
            break
        except UnboundLocalError:
            print("That isn't a correct selection. Please try again.")
            screener()

if __name__ == "__main__":
    screener()
