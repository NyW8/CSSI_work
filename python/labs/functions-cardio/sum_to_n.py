"""sum_to_n.py 

This program returns the sum of all the numbers before the number given
e.g. if you give it sum_to_n(5), it will return 5+4+3+2+1 = 15.
"""

def sum_to_n(num):
    if (num == 1):
        return 1;
    else:
        return num+sum_to_n(num - 1)
