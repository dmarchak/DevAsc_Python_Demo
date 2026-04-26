#! /usr/bin/env python3
"""Demonstrate a simple module-level constant and output."""

MY_COOL_VARIABLE = 42
print(MY_COOL_VARIABLE)

# Match Statements
CODE = 200
match CODE:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown status code")

# FOR loops example
CARS = ["Toyota", "Honda", "Ford"]
for car in CARS:
    print(car)
