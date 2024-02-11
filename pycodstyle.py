#!/usr/bin/python

def calculate_square(number):
    """Calculate the square of a given number."""
    return number ** 2


def main():
    """Entry point of the program."""
    user_input = float(input("Enter a number: "))
    result = calculate_square(user_input)
    print(f"The square of {user_input} is {result:.2f}")


if _name_ == "_main_":
    main()
