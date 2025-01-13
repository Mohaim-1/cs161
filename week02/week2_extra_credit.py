# Katie Fournier
# CS 161, Week 2
# Extra credit: Two's complement

# Repeats a prompt until the user enters a valid integer
number = None
while number is None:
    print("Enter an integer: ", end='')
    try:
        number = int(input())
        if number < -127 or number > 127:
            raise ValueError
    except ValueError:
        print("Must be an integer between -127 and 127 inclusive.")

if number >= 0:
    twos_complement = bin(number)
else:
    twos_complement = bin(number + 2**8)

# Remove "0b" prefix and always display all 8 bits
# print(twos_complement)
print(f"{twos_complement[2:]:0>8s}")
