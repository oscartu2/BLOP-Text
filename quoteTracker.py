
import requests
from tkinter import *
from tkinter import ttk

def refresh(interval):
	# Updates the stocks and direction of the pricing with red/green arrows
	# for every specified interval of time
	print("test")

def search(ticker):
	# Automatically webscrape stock information 
	url = "http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker)
	response = requests.get(url)


def draw():
	# Draw the GUI?
	# GUI: Displays a list of stock symbols with current price, previous price, 
	# and direction it has gone (up or down) since last refresh. 
	# Possible also to show refreshed X times since launch, and other logistics.
	root = Tk()
	root.title("Quote Tracker 9000")
	mainframe = ttk.Frame(root, padding = "3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)
	root.mainloop()


def prompt():
	# Prompts users to enter in list of symbols of stocks and interval to refresh
	print("testp")
	ticker = input("This is a quote tracker. Key in the ticker symbol to get current data: ")
	search(ticker)

def main():
	prompt()
	draw()



if __name__ == "__main__":
	main()