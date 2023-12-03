#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
s = "Last digit of"
if number < 0 and last != 0:
    print(s" {} is -{} and is less than {} and not 0".format(number, last, 6))
elif last > 5:
    print(s" {} is {} and is greater than {}".format(number, last, 5))
elif last == 0:
    print(s" {} is {} and is {}".format(number, 0, 0))
elif last < 6 and number > 0:
    print(s" {} is {} and is less than {} and not 0".format(number, last, 6))
