"""Intro to Python - Part 1 - Hands-On Exercise."""

import math
import random

pi = math.pi

print(pi,type(pi))

picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == 'orange':
    print("The fruit is orange")
elif picked_fruit == 'strawberry':
    print("The fruit is red")
elif picked_fruit == 'banana':
    print("The fruit is yellow")




def mult_number(add1,add2):
    result = add1*add2
    return result

print("12 x 96 =", mult_number(12, 96))

print("48 x 17 =", mult_number(48, 17))

print("196523 x 87323 =", mult_number(196523, 87323))
