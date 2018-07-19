#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")
    
    choice = input("Enter your choice [a|b|c|d|e]:")
    
    # Your code below! Handle the cases when the user chooses a, b, c, d, or e

    if choice == "a":
        adder = input("What would you like to add? Separate values with commas: ").lower()
        adder = adder.split(",")
        for add in adder:
            if add in shopping_list:
                print(add+" is already on the list!")
            else:
                shopping_list.append(add)
                print(add+" has been added to the list.")
    elif choice == "b":
        remover = input ("What would you like to remove? ").lower()
        if (remover in shopping_list):
            a = input("Are you sure you would like to remove "+remover+" y/n ")
            if a =="y":
                shopping_list.remove(remover)
            else:
                print("Cancelled")
        else:
            print("I'm sorry, that was not found in the list.")
    elif choice == "c":
        checker = input("What would you like to check for? ").lower()
        if checker in shopping_list:
            print("That item is in your list already!")
        else:
            a = input("That item is not currently in your list, would you like to add "+checker+" y/n")
            if a =="y":
                shopping_list.append(checker)
    elif choice == "d":
        for thing in shopping_list:
            print (thing)
