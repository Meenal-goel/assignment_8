#1- What is Time Tuple?
print("In Python Time Tuple, We represent time in a way that’s easy for us to understand. However, Python stores it in tuples. These python tuples are made of nine numbers.This tuple has an equivalent struct_time structure.")
'''
Index	Field	        Domain of Values
0	Year             (4 digits)	Ex.- 1995
1	Month            1 to 12
2	Day	         1 to 31
3	Hour	         0 to 23
4	Minute	         0 to 59
5	Second	         0 to 61 (60/61 are leap seconds)
6	Day of Week	 0 to 6 (Monday to Sunday)
7	Day of Year	 1 to 366 (Julian day)
8	DST	        -1,0,1
Leap seconds are added to make up to Earth’s slowing rotation. When DST is 0, it isn’t applied. When it’s 1, it is applied. However, when it is -1, it is up to the library to determine that.
'''
print("\n")
#2-Write a program to get formatted time.

import datetime
present = datetime.datetime.now()
print("FORMATTED TIME IS :",present.strftime("%a %b %y %H:%M:%S %p"))
print("\n")

#3-Write a program extract month from time

import time
x = time.gmtime()
print("Month extracted from time is:",x.tm_mon)
print("\n")

#4- Extract day from the time.

import time
x = time.gmtime()
print("Day extracted from time is:",x.tm_mday)
print("\n")

#5-Extract date,month.year,hour ,second from specific time

import datetime
dt = datetime.datetime(2021,1,11)
print(dt.day)
print("\n")

#6-Write a program to print time using localtime method.
import time;

local = time.localtime(time.time())
print ("Local current time :", local)
print("\n")

#7- Find the factorial of a number input by user using math package functions.

import math
num = int(input("enter a number:"))
print("the factorial of %d is :"%(num),math.factorial(num))
print("\n")

#8- Find the GCD of a number input by user using math package functions.

import math
numx = int(input("enter a number:"))
numy = int(input("enter a number:"))
print("the gcd of %d , %d is :"%(numx,numy),math.gcd(numx, numy))
print("\n")

#9-Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.

import os

print("current working directory is :",os.getcwd())
print("user environment is :",os.name)


