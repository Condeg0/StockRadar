import yfinance as yf
import pandas

STOCK = "aapl"


# define function to get information about the stock
def get_info(ticker):  # add try except statement
    stock = yf.Ticker(ticker)

    # create a list and a dict to hold all relevant values - Valuation, Efficiency and Financials (in order)
    relevant_info_list = ["dividendYield", "trailingPE", "priceToSalesTrailing12Months", "revenuePerShare",
                          "priceToBook", "returnOnAssets", "debtToEquity", "returnOnEquity", "totalRevenue",
                          "totalDebt", "freeCashflow", "profitMargins", "marketCap", "industry", "industryKey", "open"]
    relevant_info_dict = {}

    # add financial information to the dictionary
    for item in relevant_info_list:
        relevant_info_dict[item] = stock.info[item]

    # creates a pandas dataframe for holding price history (1Y)
    price_hist = stock.history(period="1Y")
    year_return = (price_hist["Close"].iloc[0] / price_hist["Close"].iloc[-1]) - 1 # calculates 12M return
    relevant_info_dict["yearlyReturn"] = year_return

    return relevant_info_dict


# ===== JP =====
# pandas - data frame manipulation (may not be necessary)
# yfinance library - price history
# # obs: get dataframe, clean it (remove unnecessary columns) and generate an image me frame (1d, 1w, 1m, 12m, 5y, all)
# Defines function to get the graph based on two arguments - ticker and tf
 # example - call get_graph function from company_info.py with two arguments - stock name (ticker) and the time-
 # frame (tf). time frame selected can be retrieved by calling event.widget.cget("text"), which gets the name of
 # button  pressed- check doc
def get_graph(ticker, tf):
    stock = yf.Ticker(ticker)

    # Creates a pandas dataframe for holding price history information for (1Y)
    price_hist = stock.history(period="1Y")

    # Generates graph ===== JP =====
    graph = 0   # jpeg file or other file format

    return graph
