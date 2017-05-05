
def countVowels(s):
	count = 0
	for char in s:
		if (char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u' ):
			count = count + 1

	return count

def main():
	s = raw_input('Enter a word to count vowels: ')
	count = countVowels(s)
	print s + ' has ' + str(count) + ' vowels.'

if __name__ == "__main__":
	main()