"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
	print(" It is less than 50")

elif i > 50:
	print(" It is greater than 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

print(picked_fruit)

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiplication(a, b):
	c = a * b
	return c

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", multiplication(12, 96))

print("48 x 17 =", multiplication(48, 17))

print("196523 x 87323 =", multiplication(196523, 87323))
