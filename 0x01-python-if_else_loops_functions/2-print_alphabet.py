#!/usr/bin/python3

def print_alphabet() -> None:

    for letter in range(97, 123):
        print("{:c}".format(letter), end="")


if __name__ == "__main__":
    print_alphabet()
