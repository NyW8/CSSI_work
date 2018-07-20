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
import time
# Replace "pass" with your code
class Transaction(object):
    def __init__(self, type, amount, src_acct, dest_account = 0):
        dest_account = dest_account or ""
        self.time = time.time()
        self.type = type
        self.amount = amount
        self.src_acct = src_acct
        self.dest_account = dest_account
        if type == "withdraw":
            self.src_acct.withdraw(float(self.amount))
        elif type == "deposit":
            self.src_acct.deposit(float(self.amount))
        elif type == "transfer":
            self.src_acct.transfer(self.dest_account, float(self.amount))

    def __str__(self):
        returnStr = str(self.time)+": "+self.type+" $"+str(self.amount)
        if self.dest_account != "":
            returnStr +=" to account "+self.dest_account
        return returnStr


class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance

    def __str__(self):
        return ("label: "+self.label+" balance: "+str(self.balance))

    def withdraw(self, num):
        if num < 0:
            print ("You cannot take out negative money!")
        elif self.balance - float(num) <0:
            print("You do not have enough money!")
        else:
            self.balance -=float(num)
            print("$"+str(num)+" has been withdrawn")

    def deposit(self, num):
        if num < 0:
            print("You cannot add negative money!")
        else:
            self.balance+=float(num)
            print("Successfully deposited $"+str(num))

    def rename(self, label):
        if (label == ""):
            print("Cannot name it blank!")
        else:
            self.label = label

    def transfer(self, dest_account, amount):
        if amount > self.balance:
            print("Cannot transfer more money than you have!")
        elif amount < 0:
            print("Cannot transfer negative amount!")
        else:
            dest_account.deposit(float(amount))
            self.balance-= float(amount)
