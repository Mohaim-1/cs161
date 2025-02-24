# Katie Fournier
# CIS 161 Week 7


import random


def input_int(prompt: str, **kwargs) -> int:
    """Prompts the user for an integer and repeats the prompt until it's valid."""

    num = None
    while num is None:
        try:
            num = int(input(prompt))
            if 'minimum' in kwargs.keys():
                if num <= kwargs['minimum']:
                    print(f'Must be at least {kwargs["minimum"]}')
                    num = None
        except ValueError:
            print('Must be an integer')
    return num


def evens():
    """Prints all even numbers in a range from user input."""

    lower_num = input_int('Enter the lower number:  ')
    upper_num = input_int('Enter the higher number:  ', minimum=lower_num)
    while upper_num < lower_num:
        upper_num = input_int('Enter the higher number:  ')
        if upper_num < lower_num:
            print('The higher number must be at least the lower number')
    evens = [str(i) for i in range(lower_num + (lower_num % 2), upper_num + 1, 2)]
    print(f'The even numbers between {lower_num} and {upper_num} are:', ' '.join(evens))


def factors():
    """Prints the factors of an integer."""

    number = input_int('Enter a positive integer:  ', minimum=1)
    # Factors of a number can't be larger than number / 2
    print(f'The integers that are factors of {number} are:  1 ', end='')
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            print(f'{i} ', end='')
    print(number)


def name_letters():
    """Prints the sum of the ordinal positions of the letters in my name, with a = 0, b = 1, etc."""

    alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    name = 'katherine'
    total = 0
    for c in name.lower():
        total += alphabet.index(c)
    print(f'Sum of the numeric positions of the letters in {name}: {total}')


def squares(maximum: int):
    """Prints all numbers up to the maximum squared using recursion."""

    if maximum > 1:
        squares(maximum - 1)
    print(int(maximum**2))


def swap(nums, l, r):
    """Swaps two values in a list."""

    l_val = nums[l]
    nums[l] = nums[r]
    nums[r] = l_val


def insertion_sort(nums):
    """Sorts a list via insertion sort."""

    for i in range(len(nums)-1):
        j = i
        while j >= 0 and nums[j+1] < nums[j]:
            swap(nums, j, j+1)
            j -= 1


def teepee_sort(nums):
    """Sorts a list of integers such that it's arranged like so:
        lowest to highest odd values, largest value, highest to lowest even values
    You can imagine it would form a teepee shape, from low to high to low again.
    """
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens += [num]
        else:
            odds += [num]
    insertion_sort(odds)
    insertion_sort(evens)
    return odds + evens[-1:0:-1]


def next_highest(num: int, depth=1):
    # TODO: Implement
    pass


# evens()
# factors()
# name_letters()
# squares(4)

unsorted_list = [12, 43, 22, 34, 2, 21, 3, 33, 81]
print(teepee_sort(unsorted_list))


