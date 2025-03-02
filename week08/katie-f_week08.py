# Katie Fournier
# CS 161 Winter 2025


from time import perf_counter_ns
import os
import sys


def input_nonempty(prompt: str) -> str:
    input_string = ''
    while input_string == '':
        input_string = input(prompt)
    return input_string


def probs_1_2_3_4():
    """Implementation of problems 1, 2, 3, and 4."""

    # Problem 1
    prompt = "Enter a phrase: "
    phrase_1 = input_nonempty(prompt)
    phrase_2 = input_nonempty(prompt)
    if phrase_2 == phrase_1.upper():
        print("Stop shouting please!")
    print()

    # Problem 2
    remaining_vowels = ['a','e','i','o','u']
    string = input_nonempty("Enter a string: ")
    unique_vowels = 0
    for char in string.lower():
        if char in remaining_vowels:
            unique_vowels += 1
            remaining_vowels.remove(char)
    print((f"{string} has {unique_vowels} different vowel{'s' if unique_vowels != 1 else ''}\n"))

    # Problem 3
    string_1 = input_nonempty("Enter a string: ")
    string_2 = input_nonempty("Enter another string: ")
    if string_1 != string_2:
        print(f"{min(string_1, string_2)} comes before {max(string_1, string_2)}")
    else:
        print(f"you entered {string_1} twice")
    print()

    # Problem 4
    while True:
        email_1 = input_nonempty("Enter your email address: ")
        email_2 = input_nonempty("Enter your email address again: ")
        if email_1 == email_2:
            break
        print("The two inputs did not match.")
    print("Thank you!")


pos_int_err_msg = "must be a positive integer"


def factorial_iter(integer):
    """Calculates the factorial of a number using an iterative approach and
    prints and returns the result.
    """

    if integer < 1:
        raise ValueError(pos_int_err_msg)

    factorial = 1
    for i in range(integer):
        factorial *= i + 1

    print(factorial)
    return factorial


def factorial_recurs_nested(integer):
    """Calculates the factorial of a number using a recursive approach and
    returns the result.
    """

    if integer <= 1:
        return 1
    return integer * factorial_recurs_nested(integer - 1)


def factorial_recurs(integer):
    """Calculates the factorial of a number using a recursive approach and
    prints and returns the result.
    """

    if integer < 1:
        raise ValueError(pos_int_err_msg)

    # Use another function that doesn't print the result. The same could be 
    # accomplished with an optional parameter for this function (e.g. mute=False),
    # but it'd be slow to have to check it during every recursive call.
    factorial = factorial_recurs_nested(integer)

    print(factorial)
    return factorial


def pretty_table(data, column_labels):
    """Prints a pretty table of values with column labels. Column widths are
    determined by the length of the column labels. 
    """

    spacing = 2
    # Column width is determined by the column labels
    # Minimum column width is 1
    column_labels = [(label if label != '' else ' ') for label in column_labels]
    col_widths = [len(label) for label in column_labels]

    # Column labels
    print((' ' * spacing).join(column_labels))
    # Dividing line
    print((' ' * spacing).join(['-' * len(label) for label in column_labels]))

    for row in data:
        for i in range(min(len(row), len(column_labels))):
            cell = str(row[i])
            # Truncate if needed
            if len(cell) > col_widths[i]:
                cell = cell[:col_widths[i]-1] + '…'
            print(' ' * (spacing if i > 0 else 0) + cell.rjust(col_widths[i]), end='')
        print()


def benchmark_iter_vs_recurs():
    """Measures the execution times of an iterative and a recursive approach to
    calculating a factorial and prints the results in a table.
    """

    test_values = [3, 10, 25,
                   # 40, 60, 80, 100
                   ]
    results = []
    # Suppress the tested functions' printing
    sys.stdout = open(os.devnull, 'w')

    for val in test_values:

        # Repeat the test for more consistent results
        iter_times = []
        recurs_times = []
        for i in range(1000):

            # Time the iterative approach
            start = perf_counter_ns()
            factorial_iter(val)
            stop = perf_counter_ns()
            iter_times += [stop - start]

            # Time the recursive approach
            start = perf_counter_ns()
            factorial_recurs(val)
            stop = perf_counter_ns()
            recurs_times += [stop - start]

        iter_avg_time = int(sum(iter_times)/len(iter_times))
        recurs_avg_time = int(sum(recurs_times)/len(iter_times))
        results += [[val,
                     iter_avg_time,
                     recurs_avg_time,
                     # int(iter_avg_time / val),
                     # int(recurs_avg_time / val)
                     ]]

    # Re-enable printing
    sys.stdout = sys.__stdout__

    column_names = ['Input', 'Iterative', 'Recursive',
                    #'Iter/n', 'Recurs/n'
                    ]
    pretty_table(results, column_names)
    # Tested with larger integers along with data about time div. by integer (shown above, commented out).
    # It appears that the recursive approach is slightly faster for small integers and slower for
    # larger integers. The relative difference stabilizes as the integer increases, and it settles
    # on the recursive approach being ~20% slower than the iterative approach. Both methods are O(n).


probs_1_2_3_4()
print()

# Problem 5
benchmark_iter_vs_recurs()


