"""roll_dice.py

Rolls random dice
"""
import random

def roll_dice(num):
    total = 0
    for x in range(0, num):
        die = random.randint(1,6)
        total += die
    return total
    
