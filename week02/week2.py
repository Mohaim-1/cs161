# Katie Fournier
# CS 161, Week 2

import sys


def part_1():

    # Problems 1 and 2
    # bin() and hex() take an integer.
    # If x is the wrong data type (such as a float), we get a TypeError.
    try:
        x = 18
        print(x, bin(x), hex(x))
    except TypeError:
        sys.exit("x must be an integer.")

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
        sys.exit("original size and compressed size must be positive.")
    compression_amount = f"{1 - (total_compressed_size / original_size):.2%}"

    print((f"\n"
           f"Compressed text size: {compressed_text_size} characters\n"
           f"     Dictionary size: {dictionary_size} characters\n"
           f"               Total: {total_compressed_size} characters\n"
           f"  Original text size: {original_size} characters\n"
           f"         Compression: {compression_amount}"))


part_1()
compression()
