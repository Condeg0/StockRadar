import yfinance as yf


# define function to get information about the stock
def get_info(ticker):
    stock = yf.Ticker(ticker)

    # create a list and a dict to hold all relevant values
    relevant_info_list = ["dividendYield", "trailingPE", "priceToSalesTrailing12Months", "returnOnAssets", "returnOnEquity", "revenuePerShare", "totalRevenue", "totalDebt", "freeCashflow", "debtToEquity", "profitMargins", "marketCap", "industry", "industryKey"]
    relevant_info_dict = {}

    # add financial information to the dictionary
    for item in relevant_info_list:
        relevant_info_dict[item] = stock.info[item]

    return relevant_info_dict

print(get_info("aapl"))
