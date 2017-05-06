
def isPalindrome(s):
	front = 0
	back = len(s) - 1
	for i in range(len(s)/2):
		if (s[front].lower() != s[back].lower()):
			return False
		front += 1
		back -= 1
	return True


def main():
	s = raw_input('Please enter a word: ')
	print 'Is ' + s + ' a palindrome? '
	print isPalindrome(s)

if __name__ == "__main__":
	main()