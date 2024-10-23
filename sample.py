# Sample python file
import os


def greet_user(name):
    """Greets the user"""
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Guest!")


# This is a function that tries to open an environment variable
def get_secret_key():
    """Gets the secret key from environment variable"""
    return os.getenv("SECRET_KEY")


# Main function
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet_user(user_name)
    secret_key = get_secret_key()
    if secret_key:
        print("Secret key is found!")
    else:
        print("No secret key found.")
