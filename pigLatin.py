

def is_vowel(char):
    return (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u')

def translate(string):
    vowel_seen = False
    rest_of_string = ''
    ending = ''
    for char in string:
        if (not is_vowel(char) and not vowel_seen):
            ending = ending + char
        else:
            rest_of_string = rest_of_string + char
            vowel_seen = True
            
    return rest_of_string + ending + 'ay'

def main():
    s = raw_input('Enter a word to be translated to Pig Latin: ')
    print translate(s)
    
if __name__ == "__main__":
    main()