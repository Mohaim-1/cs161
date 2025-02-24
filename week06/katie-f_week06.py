# Katie Fournier
# CIS 161 Week 6


def input_int(prompt:str, minimum = 0) -> int:
    """Prompts the user for an integer, repeats until it's valid, and returns it."""

    integer = None
    while integer is None:
        try:
            integer = int(input(prompt))
            if integer < minimum:
                print(f'must be at least {minimum}')
                integer = None
        except ValueError:
            print('must be an integer')

    return integer


def countdown():
    """Prompts the user for an integer then counts down to zero."""

    number = input_int('enter an integer: ')
    decrement = input_int('enter decrease: ', 1)

    while number > 0:
        print(f"{number} is {'even' if number % 2 == 0 else 'odd'}")
        number -= decrement
    print('blastoff!!')


def word_game_1(messages):
    """Prompts the user endlessly until they enter a word that's shorter than 5 characters.

    Parameters
    ----------
    messages : dict
        For localization. Dictionary of strings printed to the user
    """

    input_word = ''
    while input_word == '' or len(input_word) >= 5:
        input_word = input(messages['prompt'])
        word_len = len(input_word)
        if word_len == 0:
            continue
        print(messages['count'].format(
            word = input_word,
            count = word_len,
            letters = messages['letters'] if word_len > 1 else messages['letter']))
    print(messages['win'])


def word_game_2(messages):
    """Prompts the user until they enter a word that's shorter than 5 characters.
    If they enter more than 5 words, they lose.

    Parameters
    ----------
    messages : dict
        For localization. Dictionary of strings printed to the user
    """

    input_word = ''
    tries = 0
    while input_word == '' or len(input_word) >= 5:
        input_word = input(messages['prompt'])
        word_len = len(input_word)
        if word_len == 0:
            continue
        print(messages['count'].format(
            word = input_word,
            count = word_len,
            letters = messages['letters'] if word_len > 1 else messages['letter']))
        tries += 1
        if tries > 5:
            print(messages['lose'])
            return
    print(messages['win'])


def count_10_to_100():
    """Counts from 10 to 100 in decimal, binary, and hex."""

    number = 10
    while number <= 100:
        print(number, bin(number), hex(number))
        number += 1


def sum_of_digits(num: int) -> int:
    """Returns the sum of the digits of an integer."""

    if not isinstance(num, int):
        raise TypeError(f'must be int, not {type(num).__name__}')

    if num == 0:
        return 0
    return abs(num) % 10 + sum_of_digits(int(num/10))


def is_palindrome(text: str) -> bool:
    """Returns true if a string is a palindrome."""

    if not isinstance(text, str):
        raise TypeError(f'must be str, not {type(text).__name__}')

    if text == '':
        return True
    text = text.lower()
    return text[0] == text[-1] and is_palindrome(text[1:-1])


def extra_credit_2():
    """Prompts for a string and prints if it's a palindrome or not."""

    text = ''
    while text == '':
        text = input('Check if Palindrome: ')
        if text == '':
            print('Must be a non-empty string')

    if is_palindrome(text):
        print(f'Yes, {text} is a Palindrome')
    else:
        print(f'No, {text} is not a Palindrome')



def draw_triangle_iter(size):
    """Prints a triangle pattern using iteration."""

    for i in range(size, 0, -1):
        print('*' * i)


def draw_triangle_recurs(size):
    """Prints a triangle pattern using recursion."""

    if size == 0:
        return
    print('*' * size)
    draw_triangle_recurs(size - 1)


# Problems 1-3
countdown()
print()

messages_eng = {'prompt':  'enter a word: ',
               'count':   '{word} has {count} {letters}',
               'letter':  'letter',
               'letters': 'letters',
               'win':     'goodbye',
               'lose':    'loser'}

# Problem 4.1
word_game_1(messages_eng)
print()

# Problem 4.2
word_game_2(messages_eng)
print()

# Problem 5
count_10_to_100()
print()

# Problem 6
draw_triangle_iter(5)
print()
draw_triangle_recurs(7)
print()

# Extra credit 1
print(sum_of_digits(1234))
print()

# Extra credit 2
extra_credit_2()


