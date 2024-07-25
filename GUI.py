import tkinter as tk
from tkinter import ttk
import ttkthemes
from PIL import Image, ImageTk
import humanize
import company_info


# ===== Sets up Global variables =====

SMALL_FONT = "Arial 11"
BIG_FONT = "ARIAL 14"
THEME = "plastik"  # Choose theme in https://pypi.org/project/TKinterModernThemes/
ROW1 = 100
ROW2 = 600
ROW3 = 1000
COLUMN1 = 400
COLUMN2 = 600
COLUMN3 = 800
COLUMN4 = 1000
GRAPH_PATH = "/home/rafaelconde/Research/Histogram - S&P500 weekly return.png"


# ===== Sets up the GUI functionality =====

# On mouse click, clear the search bar and place cursor at first position
def clear_search_bar(event):
    event.widget.delete(0, tk.END)


# Sets the search button functionality - on click, sets all labels
def define_labels():  # requires one argument (a dictionary from company_info.get_info())
    # Gets the input from search_bar and assigns it to function get_info - returns a dictionary
    financial_dict = company_info.get_info(search_bar.get())  # add try except statement on get_info function

    price_label.config(text=f"Open price:\n${financial_dict["open"]}", font=BIG_FONT)
    market_cap_label.config(
        text=f"Market Cap:\n{humanize.intword(financial_dict["marketCap"]).replace(" trillion", "T")}", font=BIG_FONT)
    dividend_yield_label.config(text=f"Dividend Yield:\n{(100 * financial_dict["dividendYield"]):.2f}%", font=BIG_FONT)
    return_label.config(text=f"12M Return:\n{financial_dict["yearlyReturn"]:.2f}%", font=BIG_FONT)
    pe_label.config(text=f"Price/Earnings:\n{financial_dict["trailingPE"]:.0f}", font=BIG_FONT)
    pts_label.config(text=f"Price/Sales:\n{financial_dict["priceToSalesTrailing12Months"]}")
    rps_label.config(text=f"Revenue per Share:\n{financial_dict["revenuePerShare"]}")
    pb_label.config(text=f"Price/Book:\n{financial_dict["priceToBook"]}")
    roa_label.config(text=f"ROA:\n{financial_dict["returnOnAssets"]}")
    dte_label.config(text=f"Debt to Equity:\n{financial_dict["debtToEquity"]}")



# ===== JP =====
def get_price_graph(ticker, tf):
    # example - call get_graph function from company_info.py with two arguments - stock name (ticker) and the time
    # frame (tf) time frame selected can be retrieved by calling event.widget.cget("text"), which gets the name of
    # button  pressed - check doc
    graph = company_info.get_graph("aapl", "1d")

    return graph


# ===== Sets up the GUI interface ======
# Sets up the window: title and size
window = tk.Tk()
window.title("Stock Analyzer")
window.minsize(width=1500, height=900)

# Sets up the styles - to choose!
style = ttkthemes.ThemedStyle(window)
style.set_theme(THEME)

# Sets the search bar and search button
""" Functionality to add - make it interactive, error handling (error message), ability to suggest"""
search_bar = ttk.Entry(width=25, font=SMALL_FONT)
search_bar.insert(0, "Search Companies")
search_bar.place(x=650, y=15)
search_bar.bind("<FocusIn>", clear_search_bar)
ticker = search_bar.get()

search_button = ttk.Button(text="🔎", width=5, command=define_labels)
search_button.place(x=860, y=15)

# Sets ROW1 labels - current price, market cap, dividend yield and 12M return
price_label = ttk.Label(text=f"Open price:", font=BIG_FONT)
price_label.place(x=COLUMN1, y=ROW1)
market_cap_label = ttk.Label(text=f"Market Cap:", font=BIG_FONT)
market_cap_label.place(x=COLUMN2, y=ROW1)
dividend_yield_label = ttk.Label(text=f"Dividend Yield:", font=BIG_FONT)
dividend_yield_label.place(x=COLUMN3, y=ROW1)
return_label = ttk.Label(text=f"12M Return:", font=BIG_FONT)
return_label.place(x=COLUMN4, y=ROW1)

# Sets the price graph and graph buttons
graph = Image.open(GRAPH_PATH)  # Open image file with Pillow
graph_image = ImageTk.PhotoImage(graph)  # convert image to PhotoImage object
price_graph_label = ttk.Label(image=graph_image)  # create a ttk label and set the image
price_graph_label.place(x=400, y=200)

one_day_button = ttk.Button(text="1D", command=get_price_graph, width=3)  # 1D button
one_day_button.place(x=400, y=200)
five_days_button = ttk.Button(text="5D", command=get_price_graph, width=3)  # 5D button
five_days_button.place(x=430, y=200)
one_month_button = ttk.Button(text="1M", command=get_price_graph, width=3)  # 1M button
one_month_button.place(x=460, y=200)
three_month_button = ttk.Button(text="3M", command=get_price_graph, width=3)  # 3M button
three_month_button.place(x=490, y=200)
ytd_button = ttk.Button(text="YTD", command=get_price_graph, width=4)  # YTD button
ytd_button.place(x=520, y=200)
max_button = ttk.Button(text="MAX", command=get_price_graph, width=5)
max_button.place(x=555, y=200)

# Sets Row 2 labels (valuation indicators) - P/E, P/B, Revenue per share, Price to Sales
pe_label = ttk.Label(text=f"Price/Earnings", font=SMALL_FONT)  # price earnings
pe_label.place(x=COLUMN1, y=ROW2)
pts_label = ttk.Label(text="Price/Sales", font=SMALL_FONT)  # price to sales
pts_label.place(x=550, y=ROW2)
rps_label = ttk.Label(text="Revenue Per Share", font=SMALL_FONT)  # revenue per share
rps_label.place(x=680, y=ROW2)
pb_label = ttk.Label(text="Price/Book", font=SMALL_FONT)  # Price to Book
pb_label.place(x=850, y=ROW2)

# === ADD FROM HERE TO FUNCTION define_labels ===
# Valuation Info

# Efficiency indicators
roa_label = ttk.Label(text="ROA", font=SMALL_FONT)  # Return on Assets
roa_label.place(x=ROW3, y=COLUMN1)
dte_label = ttk.Label(text="Debt to Equity", font=SMALL_FONT)  # Debt to Equity
dte_label.place(x=ROW3, y=COLUMN2)

window.mainloop()
