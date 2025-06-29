# Standard library imports
import sys
import os

# Third-party imports (if any)
# import requests

# Local application imports (if any)
# from mymodule import myfunction


def greet(name):
    """Function to greet a person by name."""
    print(f"Hello, {name}!")


class Person:
    """A simple Person class."""
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hi, I'm {self.name}.")


def main():
    """Main function to run when the script is executed directly."""
    greet("World")
    person = Person("Alice")
    person.say_hello()


if __name__ == "__main__":
    main()