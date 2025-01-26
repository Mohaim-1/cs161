# Katie Fournier
# CS 161 Winter 2025
# Week 3 Assignment

import csv
import sys

# Problems 1-3
def main():

    # Problem 1
    name = input("What is your name? ")
    print("Hello " + name)

    # Problem 2
    age = input_int("What's your age? ")
    # input() outputs a string. You cannot do math on a string.
    # The age variable must be converted to a number (which it has).
    print(age + 5)

    # Problem 3
    added_years = input_int("How many years to add to your age? ")
    older_age = age + added_years
    year_str = "year"
    print(("In " + str_with_units(added_years, year_str) + " you will be "
          + str_with_units(older_age, year_str) + " old"))

    # Extra Credit
    with open("ssa_life_expectancy.csv", newline='') as life_expectancy_table:
        reader = csv.reader(life_expectancy_table)
        headings = next(life_expectancy_table)
        if headings[0] != "age" or headings[1] != "male" or headings[2] != ["female"]:
            sys.exit(("Expected ssa_life_expectancy.csv with first row as follows:\n"
                      "age,male,female"))
        life_expectancy = []
        for row in reader:
            life_expectancy.append({row{"age"}, 
    
    print(("The SSA provides life expectancy data for males and females.\n"
        "Males of your age are expected to live ${life_expectancy[age][0]}"))

def input_int(prompt) -> int:
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except TypeError:
            print("Please enter an integer.")
    return number


def str_with_units(number, unit, plural_unit=None) -> str:
    """Takes an integer and returns it as a string along with its specified units, singular or plural."""

    if number == 1:
        unit_word = unit
    else:
        if plural_unit is not None:
            unit_word = plural_unit
        else:
            unit_word = unit + "s"
    return str(number) + " " + unit_word


main()
