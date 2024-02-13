#!/usr/bin/python3

def greet(name):
    """
    Greets the user with a friendly message.
    Args:
        name (str): The name of the person to greet.
    Returns:
        str: A personalized greeting.
    """
    return f"Hello, {name}! Welcome to our program."


def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))


if _name_ == "_main_":
    main()
