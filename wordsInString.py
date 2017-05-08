
def read_file():
	count = 0
	filename = raw_input("Please enter the file name exactly: ")
	with open(filename) as f:
		for word in f.read().split():
			count += 1
	return count

def read_string():
	count = 0
	s = raw_input("Please enter the string to count words in: ")
	for word in s.split():
		count += 1
	return count

def main():
	num_words = 0
	input_string = raw_input("Would you like to read from a file? ")
	if (input_string.lower().startswith("y")):
		num_words = read_file()
	else:
		num_words = read_string()
	print "There are " + str(num_words) + " words in your string."

if __name__ == "__main__":
	main()