import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import humanize
import company_info

# ===== Sets up Global variables =====

WD = "/home/rafaelconde/Programing/Python/Programs/Resume Project/Resume Project"
SMALL_FONT = "Arial 11"
BIG_FONT = "ARIAL 14"
THEME = "Adapta"  # Choose theme in https://pypi.org/project/TKinterModernThemes/
ROW1 = 75
ROW2 = 550
ROW3 = ROW2 + 40
ROW4 = ROW2 + 40
COLUMN1 = 200
COLUMN2 = COLUMN1 + 200
COLUMN3 = COLUMN1 + 400
COLUMN4 = COLUMN1 + 600
GRAPH_PATH = "/home/rafaelconde/Programing/Python/Programs/Resume Project/Resume Project/fig.png"
global img_ref


# ===== Sets up the GUI functionality =====
# On mouse click, clear the search bar and place cursor at first position
def clear_search_bar(event):
    event.widget.delete(0, tk.END)


# Sets the search button functionality - on click, sets all labels
def define_labels():  # requires one argument (a dictionary from company_info.get_info())
    # Gets the input from search_bar and assigns it to function get_info - returns a dictionary
    ticker_ = search_bar.get()
    financial_dict = company_info.get_info(ticker_)

    price_label.config(text=f"Open price:\n${financial_dict['regularMarketPrice']}", font=BIG_FONT)
    market_cap_label.config(
        text=f"Market Cap:\n{humanize.intword(financial_dict['marketCap']).replace(' trillion', 'T')}", font=BIG_FONT)
    dividend_yield_label.config(text=f"Dividend Yield:\n{(100 * financial_dict['dividendYield']):.2f}%", font=BIG_FONT)
    return_label.config(text=f"12M Return:\n{financial_dict['yearlyReturn']:.2f}%", font=BIG_FONT)
    pe_label.config(text=f"Price/Earnings:\n{financial_dict['trailingPE']:.2f}")
    pts_label.config(text=f"Price/Sales:\n{financial_dict['priceToSalesTrailing12Months']:.2f}")
    rps_label.config(text=f"Revenue per Share:\n{financial_dict['revenuePerShare']:.2f}")
    pb_label.config(text=f"Price/Book:\n{financial_dict['priceToBook']:.2f}")
    roa_label.config(text=f"ROA:\n{financial_dict['returnOnAssets']:.2f}")
    dte_label.config(text=f"Debt to Equity:\n{financial_dict['debtToEquity']:.2f}")
    roe_label.config(text=f"ROE:\n{financial_dict['returnOnEquity']:.2f}")
    total_revenue_label.config(text=f"Total Revenue:\n{financial_dict['totalRevenue']}")
    total_debt_label.config(text=f"Total Debt:\n{financial_dict['totalDebt']:.2f}")
    fcf_label.config(text=f"Free Cash Flow:\n{financial_dict['freeCashflow']}")
    pft_mgn_label.config(text=f"Profit Margin:\n{financial_dict['profitMargins']:.2f}")
    industry_label.config(text=f"Industry:\n{financial_dict['industry']}")

    get_price_graph(ticker_, "1y")


def get_price_graph(ticker, tf):
    # get the pandas data frame and set up image
    company_info.get_graph(ticker, tf)
    # Open image file with Pillow
    g = Image.open("/home/rafaelconde/Programing/Python/Programs/Resume Project/Resume Project.png")
    pic = ImageTk.PhotoImage(g)  # convert image to PhotoImage object

    global img_ref
    img_ref = pic
    price_graph_label.config()  # clean graph
    price_graph_label.config(image=pic)  # set new image


# ===== Sets up the GUI interface ======
# Window: title and size
window = ThemedTk(theme=THEME)
window.title("Stock Analyzer")
window.geometry("1100x700")
window.configure(background="white")


# Style
style = ttk.Style()
style.configure('TButton', font="Arial 8", background='white', borderwidth=2)
style.configure("TLabel", background="white")

# Sets the search bar and search button
search_bar = ttk.Entry(width=25, font=BIG_FONT)
search_bar.insert(0, "Search Companies")
search_bar.place(x=450, y=15)
search_bar.bind("<FocusIn>", clear_search_bar)


search_button = ttk.Button(text="🔎", width=5, command=define_labels)
search_button.place(x=660, y=15)

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
price_graph_label.place(x=200, y=125)

one_day_button = ttk.Button(text="1D", command=lambda: get_price_graph(search_bar.get(), "1d"), width=3)  # 1D button
one_day_button.place(x=250, y=140)
five_days_button = ttk.Button(text="5D", command=lambda: get_price_graph(search_bar.get(), "5d"), width=3)  # 5D button
five_days_button.place(x=280, y=140)
one_month_button = ttk.Button(text="1M", command=lambda: get_price_graph(search_bar.get(), "1mo"), width=3)  # 1M button
one_month_button.place(x=310, y=140)
three_month_button = ttk.Button(text="3M", command=lambda: get_price_graph(search_bar.get(), "3mo"),
                                width=3)  # 3M button
three_month_button.place(x=340, y=140)
ytd_button = ttk.Button(text="YTD", command=lambda: get_price_graph(search_bar.get(), "ytd"), width=4)  # YTD button
ytd_button.place(x=370, y=140)
max_button = ttk.Button(text="MAX", command=lambda: get_price_graph(search_bar.get(), "max"), width=5)  # max button
max_button.place(x=410, y=140)

# Sets Row 2 labels (valuation indicators) - P/E, P/B, Revenue per share, Price to Sales
pe_label = ttk.Label(text=f"Price/Earnings", font=SMALL_FONT)  # price earnings
pe_label.place(x=COLUMN1, y=ROW2)
pts_label = ttk.Label(text="Price/Sales", font=SMALL_FONT)  # price to sales
pts_label.place(x=COLUMN2, y=ROW2)
rps_label = ttk.Label(text="Revenue Per Share", font=SMALL_FONT)  # revenue per share
rps_label.place(x=COLUMN3, y=ROW2)
pb_label = ttk.Label(text="Price/Book", font=SMALL_FONT)  # price to Book
pb_label.place(x=COLUMN4, y=ROW2)

# Efficiency indicators
roa_label = ttk.Label(text="ROA", font=SMALL_FONT)  # return on Assets
roa_label.place(x=COLUMN1, y=ROW3)
dte_label = ttk.Label(text="Debt to Equity", font=SMALL_FONT)  # debt to Equity
dte_label.place(x=COLUMN2, y=ROW3)
roe_label = ttk.Label(text="ROE", font=SMALL_FONT)  # return on equity
roe_label.place(x=COLUMN3, y=ROW3)
total_revenue_label = ttk.Label(text="Total Revenue", font=SMALL_FONT)  # total revenue
total_revenue_label.place(x=COLUMN4, y=ROW3)
total_debt_label = ttk.Label(text="Total Debt", font=SMALL_FONT)  # total debt
total_debt_label.place(x=COLUMN1, y=ROW4)
fcf_label = ttk.Label(text="Free Cash Flow", font=SMALL_FONT)  # free cash flow
fcf_label.place(x=COLUMN2, y=ROW4)
pft_mgn_label = ttk.Label(text="Profit Margin", font=SMALL_FONT)  # profit margin
pft_mgn_label.place(x=COLUMN3, y=ROW4)
industry_label = ttk.Label(text="Industry", font=SMALL_FONT)  # industry
industry_label.place(x=COLUMN4, y=ROW4)

window.mainloop()
