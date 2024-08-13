import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


# Set working directory
WD = "/home/rafaelconde/Programing/Python/Programs/Resume Project/Resume Project"

# define function to get information about the stock
def get_info(ticker):  # add try except statement

    headers = {'User-agent': 'Mozilla/5.0'}  # header
    url = f"https://finance.yahoo.com/quote/{ticker}/"  # url
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    web_content = str(soup.prettify())  # get web page content and turn it into a string
    content_list = web_content.split(",")

    # define relevant financial indicators
    indicators_info = {"dividendYield": "", "trailingPE": "", "priceToSalesTrailing12Months": "",
                       "revenuePerShare": "", "priceToBook": "", "returnOnAssets": "", "debtToEquity": "",
                       "returnOnEquity": "", "totalRevenue": "", "totalDebt": "", "freeCashflow": "",
                       "profitMargins": "", "marketCap": "", "industry": "", "regularMarketPrice": ""}

    # find all information in indicators_info dictionary
    for key_name in indicators_info.keys():
        for i in content_list:
            if f"{key_name}\\" in i:  #  and "raw" in i
                content = i.split(":")[-1]  # get actual indicator

                # if string contains digits, convert to float
                if re.match(r'\d', content):
                    indicators_info[key_name] = float(content)
                    break
                # if string is not empty
                elif content != "{}" and content != "":
                    content = re.sub(r'[^a-z A-Z]', '', content)  # remove punctuation
                    indicators_info[key_name] = content
                    break
                else:
                    continue

    # creates a pandas dataframe for holding price history (1Y)
    stock = yf.Ticker(ticker)
    price_hist = stock.history(period="1y")
    year_return = (price_hist["Close"].iloc[-1] / price_hist["Close"].iloc[0]) - 1  # calculates 12M return
    indicators_info["yearlyReturn"] = year_return * 100

    return indicators_info


# ===== JP =====
# pandas - data frame manipulation
# yfinance library - price history
# # obs: get dataframe, clean it (remove unnecessary columns) and generate an image me frame (1d, 1w, 1m, 12m, 5y, all)
# Defines function to get the graph based on two arguments - ticker and tf
def get_graph(ticker, tf):
    stock = yf.Ticker(ticker)

    # Creates a pandas dataframe for holding price history information for (1Y)
    price_hist = pd.DataFrame(stock.history(period=tf))
    price_hist = price_hist["Close"]
    plt.figure(figsize=(7, 3.7))
    graph = price_hist.plot()
    plt.savefig(WD)
    plt.close()
