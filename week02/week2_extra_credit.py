# Katie Fournier
# CS 161, Week 2
# Extra credit: Two's complement

import sys


def print_twos_complement():
    """Takes an integer as input and prints its two's complement."""

    # Repeats a prompt until the user enters a valid integer
    number = None
    while not valid_int(number):
        print("Enter an integer: ", end='')
        try:
            number = int(input())
            if not valid_int(number):
                raise ValueError
        except ValueError:
            print("Must be between -127 and 127")
        except EOFError:
            sys.exit("Bye!")

    if number >= 0:
        twos_complement = bin(number)
    else:
        # -127 <= number <= -1, so 0 <= (number + 2**8) <= 127
        twos_complement = bin(number + 2**8)

    # Remove "0b" prefix and always display all 8 bits
    print(f"{twos_complement[2:]:0>8s}")


def valid_int(x) -> bool:
    """Return whether a variable is an integer between -127 and 127."""
    return isinstance(x, int) and -127 <= x <= 127


print_twos_complement()