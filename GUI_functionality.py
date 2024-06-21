import tkinter as tk
from tkinter import ttk


# ===== Search bar functionality =====
# On mouse click, clear the search bar and place cursor at first position
def clear_search_bar(event):
    event.widget.delete(0, tk.END)
