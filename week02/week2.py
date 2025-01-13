# Katie Fournier
# CS 161, Week 2

def part_1():
    # Problem 1 and 2
    x = 18
    # bin() and hex() take an integer.
    # If x is the wrong data type (such as a float), we get a TypeError.
    print(x, bin(x), hex(x))

    # Problem 3
    y = 0b1011
    z = 0xA3
    print(y, z)

    # Problem 4
    w = x + y + z
    print('the sum is ', w)


def compression():
    """Calculates a compression percentage based on set values."""

    original_size = input_pos_int("Original data size: ")
    dictionary_size = input_pos_int("Dictionary size: ")
    compressed_text_size = input_pos_int("Compressed text size: ")

    total_compressed_size = dictionary_size + compressed_text_size
    compression_amount = f"{1 - (total_compressed_size / original_size):.2%}"

    print()
    print((f"Compressed text size: {compressed_text_size} characters\n"
           f"     Dictionary size: {dictionary_size} characters\n"
           f"               Total: {compressed_text_size + dictionary_size} characters\n"
           f"  Original text size: {original_size} characters\n"
           f"         Compression: {compression_amount}"))


def input_pos_int(prompt) -> int:
    """Repeats a prompt until the user enters a positive integer."""

    pos_int = 0
    while pos_int < 1:
        print(prompt, end='')
        try:
            pos_int = int(input())
            if pos_int < 1:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.")
    return pos_int


# part_1()
compression()

