#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last > 5:
    print("Last digit of {} is {} and is greater than {}".format(number, last, 5))
elif last == 0:
    print("Last digit of {} is {} and is {}".format(number, 0, 0))
elif last < 6 and number != 0:
    print("Last digit of {} is {} and is less than {} and not {}".format(number, last, 6, 0))
