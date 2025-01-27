# Katie Fournier
# CS 161 Winter 2025
# Week 3 Assignment

import sys
import urllib.request
import urllib.error
from datetime import date, timedelta
from math import floor

def probs_1_2_3_extra_credit_1():

    # Problem 1
    name = input("What is your name? ")
    print("Hello " + name)

    # Problem 2
    user_age = input_int("What's your age? ")
    # input() outputs a string. You cannot do math on a string.
    # The age variable must be converted to a number (which it has).
    print(user_age + 5)

    # Problem 3
    added_years = input_int("How many years to add to your age? ")
    older_age = user_age + added_years
    print(("In " + year_str(added_years) + " you will be " + year_str(older_age) + " old"))


    # Extra Credit 1

    # I decided to store the life expectancy data in a file, and I can only submit one file,
    # so I'm retrieving the data file from my GitHub repo.
    data_table_url = 'https://github.com/Mohaim-1/cs161/raw/refs/heads/main/week03/ssa_life_expectancy.csv'
    try:
        # The file arrives as bytes rather than as a string, so it must be decoded.
        life_expectancy_csv = urllib.request.urlopen(data_table_url).read().decode('utf-8').split()
    except urllib.error.URLError:
        sys.exit("Error retrieving ssa_life_expectancy.csv via HTTP.")

    header = life_expectancy_csv[0]
    if header != 'age,male,female':
        sys.exit("First row must be: age,male,female")

    min_age = 0
    max_age = int(life_expectancy_csv[-1].split(',')[0])
    if user_age < min_age or user_age > max_age:
        sys.exit("\nLife expectancy data is only available for people that are between "\
                 + f"{min_age} and {max_age} years old.")
    # The first row was the header, so trim that off. Also, the data is sorted, starting at 0, so
    # the row number is now the same as the age column.
    data = life_expectancy_csv[1:][user_age].split(',')
    if data[0] != str(user_age):
        sys.exit("Data is not sorted correctly.")
    # Column 0 = age, column 1 = male, and column 2 = female.
    life_expectancy = {'female': float(data[2]), 'male': float(data[1])}

    today = date.today()
    death_date = dict()
    for sex in ['female', 'male']:
        remaining_years = life_expectancy[sex]
        # A person's "age" in years goes up on their birthday, rather than after exactly 365 days,
        # since leap years exist. If timedelta supported years, we could just use a timedelta. If
        # leap years didn't exist, we could use days = years * 365. So, we use a date object to
        # move forward in whole years, which accounts for leap years, then add a timedelta of the
        # remainder converted to days.
        death_date[sex] = (
            date(year = today.year + floor(remaining_years),
                 month = today.month,
                 day = today.day)
            + timedelta(days = (remaining_years % 1) * 365))

    date_format = "%B %-d, %Y"
    print(("\nThe SSA provides life expectancy data for males and females.\n"
           f"A female of your age is expected to live until {death_date['female']:{date_format}},\n"
           f"and a male is expected to live until {death_date['male']:{date_format}}."))


def probs_4_5_extra_credit_2():

    # Problem 4
    hours_worked = input_float("Enter the number of hours worked: ")
    hourly_wage = input_float("Enter your hourly wage, without the $: ")
    weekly_earnings = hours_worked * hourly_wage
    # There aren't exactly a whole number of weeks in a year.
    print("\nYour gross pay this week is $ " + "{:.3f}".format(weekly_earnings) \
        + "\nYour estimated annual gross pay will be $ " + "{:,.0f}".format(weekly_earnings / 7 * 365))

    # Extra Credit 2
    tax_brackets = [11_600, 47_150, 100_525, 191_950, 243_725, 609_350]
    tax_percents = [10, 12, 22, 24, 32, 35, 37]
    # Assumes 40 hours a week and 50 weeks per year.
    total_before_tax = float(hourly_wage * 40 * 50)
    print((f"\nIf you were to work 40 hours per week, 50 weeks per year at ${hourly_wage:,.2f} per hour,\n"
           f"your gross yearly income would be ${total_before_tax:,.0f},"))
    # Incrementally "moves" each bracket's worth of money from the "untaxed pile", subtracts the
    # tax, and adds what remains into the "taxed pile" until there's none left in the untaxed pile.
    total_after_tax = float(0)
    i = 0
    while total_before_tax > 0:
        if i < len(tax_brackets):
            # The brackets with upper thresholds
            # What "fits" in the current bracket or what remains in the untaxed pile, whichever is less
            amount_in_bracket = min(
                tax_brackets[i] - (0 if i == 0 else tax_brackets[i-1]),
                total_before_tax)
        else:
            # The top bracket with no upper limit
            amount_in_bracket = total_before_tax
        total_before_tax -= amount_in_bracket
        total_after_tax += (1 - tax_percents[i]/100) * amount_in_bracket
        i += 1
    print(f"and your after-tax yearly income would be ${total_after_tax:,.0f}.")


def input_int(prompt) -> int:
    an_int = None
    while an_int is None:
        try:
            an_int = int(input(prompt))
        except TypeError:
            print("Please enter an integer.")
    return an_int


def input_float(prompt) -> float:
    a_float = None
    while a_float is None:
        try:
            a_float = float(input(prompt))
        except TypeError:
            print("Please enter a number.")
    return a_float


def year_str(number) -> str:
    """Takes an integer and returns it as a string along with the word 'year' or 'years'."""
    return str(number) + " year" + ("s" if number != 1 else "")


probs_1_2_3_extra_credit_1()
print()
probs_4_5_extra_credit_2()
