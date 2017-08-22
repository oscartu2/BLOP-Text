import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()


def refresh(interval):
	# Updates the stocks and direction of the pricing with red/green arrows
	# for every specified interval of time
	print "test"

def search():
	# Automatically webscrape stock information 
	print "test search"

def draw():
	# Draw the GUI?
	# GUI: Displays a list of stock symbols with current price, previous price, 
	# and direction it has gone (up or down) since last refresh. 
	# Possible also to show refreshed X times since launch, and other logistics.
	print "test draw"

def prompt():
	# Prompts users to enter in list of symbols of stocks and interval to refresh
	print "test prompt"

def main():
	draw()
	prompt()
	search()




if __name__ == "__main__":
	main()