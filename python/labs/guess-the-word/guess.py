
word = "hi"
guesses = []
guessed = False
def display_word():
    guessed2 = True
    for letter in word:
        if letter in guesses:
            print(letter),
        elif letter == " ":
            print (" "),
        else:
            print("_"),
            guessed2 = False
    return guessed2


while (guessed== False):
    guessed = display_word()
    print ("")
    if guessed:
        break
    currGuess = input("Guess a letter: ").lower()
    guesses.append(currGuess)
    print("Guesses: "),
    for guess in guesses:
        print (guess),
    print ('')
print("You guessed it!!")
