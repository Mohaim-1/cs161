# Katie Fournier
# CIS 161, Week 5

import requests
import psutil


def problems_1_2_3():
    """Solutions for CIS 161 week 5 homework problems 1, 2, and 3."""


    # Problem 1
    number = None
    while number is None:
        num_str = input("Enter a number: ")
        # The user might enter an int or a float
        try:
            number = int(num_str)
        except ValueError:
            try:
                number = float(num_str)
            except ValueError:
                number = None
    print(f"{number} is {'not ' if number % 5 != 0 else ''}divisible by 5.")
    print()


    # Problem 2

    unknown_state_msg = 'I do not know that one'

    # 2.1
    state = input("Please enter the name of a state: ").capitalize()
    if state == 'Oregon':
        print('Salem')
    elif state == 'Washington':
        print('Olympia')
    elif state == 'California':
        print('Sacramento')
    elif state == 'Colorado':
        print('Denver')
    elif state == 'New Mexico':
        print('Santa Fe')
    elif state == 'Minnesota':
        print('Saint Paul')
    else:
        print(unknown_state_msg)

    # 2.2
    state_capitals = {'Oregon':     'Salem',
                      'Washington': 'Olympia',
                      'California': 'Sacramento',
                      'Colorado':   'Denver',
                      'New Mexico': 'Santa Fe',
                      'Minnesota':  'Saint Paul'}
    print(state_capitals.get(state, "Not found"))

    # 2.3
    match state:
        case 'Oregon':
            print('Salem')
        case 'Washington':
            print('Olympia')
        case 'California':
            print('Sacramento')
        case 'Colorado':
            print('Denver')
        case 'New Mexico':
            print('Santa Fe')
        case 'Minnesota':
            print('Saint Paul')
        case _:
            print(unknown_state_msg)

    print()


    # Problem 3

    age = 18
    if age in [11, 18] or (age >= 80 and age < 90):
        article = 'an'
    else:
        article = 'a'
    print(f'Admission to the pool will cost ${pool_admission(age)} for {article} {age}-year-old.') 


def pool_admission(age: int) -> int:
    """Takes a person's age as input and returns the price of pool admission in dollars."""

    if age < 2:
        return 0
    elif age < 12:
        return 3
    else:
        return 4


# Problem 4
def count_string_in_html(url:str, substr:str, mute:bool=False) -> int:
    """Counts how many times a substring appears in the HTML of a webpage and prints the result.

    Parameters
    ----------
    url : str
        Webpage URL
    substr : str
        Substring to search for
    """

    webpage = requests.get(url)
    count = webpage.text.count(substr)
    if not mute:
        print(f'The substring "{substr}" appears {count} times in the HTML source of {url}.')
    return count


def count_processes(mute:bool=False) -> int:
    """Returns the number of processes running on the user's computer.
    Will print a message with the result by default.
    """

    proc_count = len(psutil.pids())
    if not mute:
        print(f"Number of running processes: {proc_count}")
    return len(psutil.pids())


def func_with_error_handling(func, *args) -> any:
    """Runs a function with the given arguments and handles any resulting error
    by printing a simple message.
    """

    try:
        return_value = func(*args)
        code = 0
    except:
        return_value = None
        code = 1
    print(f'Process finished with exit code {code}')
    return return_value


# Problems 1, 2, and 3
problems_1_2_3()
print()
# Problem 4
func_with_error_handling(count_string_in_html, 'http://coccbobcat.com', '160')
print()
# Problem 5
func_with_error_handling(count_processes)


