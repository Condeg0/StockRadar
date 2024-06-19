import yfinance as yf


# define function to get information about the stock
def get_info(ticker):
    stock = yf.Ticker(ticker)

    # create a list and a dict to hold all relevant values
    # create a list and a dict to hold all relevant values - Valuation, Efficiency and Financials (in order)
    relevant_info_list = ["dividendYield", "trailingPE", "priceToSalesTrailing12Months", "revenuePerShare",
                          "priceToBook", "returnOnAssets", "debtToEquity", "returnOnEquity", "totalRevenue",
                          "totalDebt", "freeCashflow",  "profitMargins", "marketCap", "industry", "industryKey"]
    relevant_info_dict = {}

    # add financial information to the dictionary
    for item in relevant_info_list:
        relevant_info_dict[item] = stock.info[item]

    return relevant_info_dict


print(get_info("aapl"))
