def prompt():
    s = raw_input('Enter in a word you would like to reverse: ')   
    return s

def reverse(string):
    rev = ''
    for char in string:
        rev = char + rev
    return rev

def main():
    string = prompt()
    reversed_string = reverse(string)
    print 'Reversed string: ' + reversed_string
    
if __name__ == "__main__":
    main()
