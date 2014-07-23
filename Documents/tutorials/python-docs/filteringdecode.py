"""
filtering an encrypted file(not mine just copied,
hopefully to unserstand it and rewrite it the way
i will understand to solve the problem.)
"""


import string

file_ = open('solutions.txt', 'r')
text = ''.join(file_.readlines())

def get_unique(text):
    """
    gets the "characters" in "text" = solutions.txt 
    if character is not in "new_text"
    then put in the new_text variable.
    """
    new_text = ''

    for character in text:
        if character not in new_text:
            new_text += character

    return new_text

def get_characters(text, exclude):
    """
    gets the charater in text = solution.txt
    if character is not in "exclude" variable
    append the character to the symbols variable.
    """
    symbols = ''

    for character in text:
        if character not in exclude:
            symbols += character

    return symbols

unique = get_unique(text)
print "this is unique: %s" % unique
alphabet = string.ascii_lowercase
print "this is the alphabet: %s" % alphabet
symbols = get_characters(unique, alphabet)
print "this is the symbols: %s" % symbols
letters = get_characters(unique, symbols)

# print letters