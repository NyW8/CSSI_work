"""fizz_buzz.py 

Returns fizz if divisible by 3, buzz if divisible by 5
"""

def fizz_buzz(num):
    for n in range(num):
        if (n%3 == 0) and (n%5 == 0):
            print("Computer: "+str(n)+": fizz buzz")
        elif n % 3==0:
            print("Computer: "+str(n)+": fizz")
        elif n % 5 == 0:
            print("Computer: "+str(n)+": buzz")

def fizzGame(num):
    if (num%3 == 0) and (num%5 == 0):
        return("fizz buzz")
    elif num % 3==0:
        return ("fizz")
    elif num % 5 == 0:
        return ("buzz")
    else:
        return num

#fizz_buzz(input("Input a number: "))

highscore = 0
play = True
while (play):
    player = True
    n= 1
    while (player):
        print("Computer: "+str(fizzGame(n)))
        n+=1
        if (str(fizzGame(n)) != str(input("Player: "))):
            player = False
            print("The correct answer was "+str(fizzGame(n))+". Your highscore is "+str(highscore)+".")
            x = input("Would you like to play again? y/n")
            if (x == "n"):
                play = False
        else:
            n+=1
            if n > highscore:
                highscore = n
