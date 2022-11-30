#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_d = abs(number) % 10
if number < 0:
    last_d = -last_d

if last_d > 5
    print(f"{str} {number:d} is {last_d:d} and is greater than 5")
elif number == 0:
    print(f"{str} {number:d} is {last_d:d} and is 0")
else:
    print(f"{str} {number:d} is {last_d:d} and is less than 6 and not 0")
