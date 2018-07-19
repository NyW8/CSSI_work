"""longest_word.py

This is a file that checks the longest word out of three words and returns it
"""

def longest_word(word1, word2, word3):
    firstCheck = None
    if (len(word1) > len(word2)):
        firstCheck = word1
    else:
        firstCheck = word2
    if (len(word3) > len(firstCheck)):
        return word3
    else:
        return firstCheck
