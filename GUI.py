import tkinter as tk
from tkinter import ttk
import ttkthemes
from PIL import Image, ImageTk
import humanize
import company_info
import GUI_functionality as G_fun

# ===== Sets up the GUI interface ======

# Global variables
SMALL_FONT = "Arial 11"
BIG_FONT = "ARIAL 14"
THEME = "plastik"  # Choose theme in https://pypi.org/project/TKinterModernThemes/
ROW1 = 100
ROW2 = 600
COLUMN1 = 400
COLUMN2 = 600
COLUMN3 = 800
COLUMN4 = 1000
COMPANY_INFO = company_info.get_info("aapl")

# Sets up the window: title and size
window = tk.Tk()
window.title("Stock Analyzer")
window.minsize(width=1500, height=900)

#
style = ttkthemes.ThemedStyle(window)
style.set_theme(THEME)

# Sets the search bar
""" Functionality to add - clean search bar text on click, make it interactive and ability to suggest. """
search_bar = ttk.Entry(width=25, font=SMALL_FONT)
search_bar.insert(0, "Search Companies")
search_bar.place(x=650, y=15)
search_bar.bind("<FocusIn>", G_fun.clear_search_bar)
ticker = search_bar.get()


# Sets search bar button
search_button = ttk.Button(text="🔎", width=5)
search_button.place(x=860, y=15)


# Sets ROW1 labels - current price, market cap, dividend yield and 12M return
price_label = ttk.Label(text=f"Open price:\n{COMPANY_INFO["open"]}", font=BIG_FONT)
price_label.place(x=COLUMN1, y=ROW1)
market_cap_label = ttk.Label(
    text=f"Market Cap:\n{humanize.intword(COMPANY_INFO["marketCap"]).replace(" trillion", "T")}", font=BIG_FONT)
market_cap_label.place(x=COLUMN2, y=ROW1)
dividend_yield_label = ttk.Label(text=f"Dividend Yield:\n{(100 * COMPANY_INFO["dividendYield"]):.2f}%", font=BIG_FONT)
dividend_yield_label.place(x=COLUMN3, y=ROW1)
return_label = ttk.Label(text=f"12M Return:\n{COMPANY_INFO["yearlyReturn"]:.2f}%", font=BIG_FONT)
return_label.place(x=COLUMN4, y=ROW1)
"""Functionality to add - calculate return: 
1 - get the 12M historical price data. 
2 - get first entry (price of 12M ago) and last entry (today's price)
3 - formula: (first_entry / last_entry - 1)  * 100
"""

# Sets the price graph
graph = Image.open("/home/conde/Research/Histogram.png")  # Open image file with Pillow
graph_image = ImageTk.PhotoImage(graph)  # convert image to PhotoImage object
price_graph_label = ttk.Label(image=graph_image)  # create a ttk label and set the image
price_graph_label.place(x=400, y=150)

# Sets Row 2 labels (valuation indicators) - P/E, P/B, Revenue per share, Price to Sales
pe_label = ttk.Label(text=f"Price/Earnings: {COMPANY_INFO["trailingPE"]:.0f}", font=BIG_FONT)
pe_label.place(x=COLUMN1, y=ROW2)

window.mainloop()
