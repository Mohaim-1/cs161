# Katie Fournier
# CS 161, Week 2

import sys


def part_1():

    # Problems 1 and 2
    # bin() and hex() take an integer.
    # If x is the wrong data type (such as a float), we get a TypeError.
    x = 18
    try:
        print(x, bin(x), hex(x))
    except TypeError:
        sys.exit("x must be an integer")

    # Problem 3
    y = 0b1011
    z = 0xA3
    print(y, z)

    # Problem 4
    w = x + y + z
    print('the sum is', w)


def compression():
    """Calculates a compression percentage based on set values."""

    original_size = 240
    dictionary_size = 25
    compressed_text_size = 148

    total_compressed_size = dictionary_size + compressed_text_size
    if original_size < 1 or total_compressed_size < 1:
        sys.exit("original size and compressed size must be positive")
    compression_amount = f"{1 - (total_compressed_size / original_size):.2%}"

    print((f"\n"
           f"Compressed text size: {compressed_text_size} characters\n"
           f"     Dictionary size: {dictionary_size} characters\n"
           f"               Total: {total_compressed_size} characters\n"
           f"  Original text size: {original_size} characters\n"
           f"         Compression: {compression_amount}\n"))


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
            print("Must be between -128 and 127")
        except EOFError:
            sys.exit("Bye!")

    if number >= 0:
        twos_complement = bin(number)
    else:
        # -128 <= number <= -1, so 0 <= (number + 2**8) <= 127
        twos_complement = bin(number + 2**8)

    # Remove "0b" prefix and always display all 8 bits
    print(f"{twos_complement[2:]:0>8s}")


def valid_int(x) -> bool:
    """Return whether a variable is an integer between -128 and 127."""
    return isinstance(x, int) and -128 <= x <= 127


part_1()
compression()
print_twos_complement()
