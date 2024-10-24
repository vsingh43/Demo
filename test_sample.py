"""
Sample Python script to demonstrate basic functionalities like greeting a user
and retrieving a secret key from environment variables.

This script:
1. Greets the user based on input.
2. Attempts to retrieve a secret key from environment variables.
"""

import os


def greet_user(name):
    """
    Greets the user by name or as 'Guest' if no name is provided.

    Parameters:
    name (str): The name of the user to greet.
    """
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Guest!")


def get_secret_key():
    """
    Retrieves the secret key from the environment variable 'SECRET_KEY'.

    Returns:
    str: The secret key if found, otherwise None.
    """
    return os.getenv("SECRET_KEY")


if __name__ == "__main__":
    # Get the user's name and greet them
    user_name = input("Enter your name: ")
    greet_user(user_name)

    # Try to retrieve the secret key from the environment
    secret_key = get_secret_key()
    if secret_key:
        print("Secret key is found!")
    else:
        print("No secret key found.")
