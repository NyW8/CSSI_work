"""get_number_input.py 

Takes in a string ONLY, asks for string again if you put in the wrong type
"""

def get_input():
    x = input("Please enter a string: ")
    while (isFloat(x)):
        x = input("Please enter a REAL string: ")
    print ("Thank you! Your string was: "+x)


def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
