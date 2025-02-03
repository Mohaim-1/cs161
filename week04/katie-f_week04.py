# Katie Fournier
# Cs 161 Week 04


import pandas
from threading import Thread, Timer
import sys


# Problems 1-7


def average(num1, num2, num3):
    """Finds the average of three numbers."""
    return (num1 + num2 + num3)/3


def cone_price(scoops):
    """Returns the cost of an ice cream cone in dollars."""
    return scoops * 1.15 + 2.25


def dog_to_human_years(dog_age):
    """Converts a dog's age in years to human years."""
    return 24 + (dog_age - 2) * 4


def car_value(purchase_price, age, country):
    """Calculates the depreciated value of a vehicle.

    Parameters
    ----------
    purchase_price : int
        Purchase price of the vehicle in dollars
    age : int
        Years since the vehicle was purchased
    country : string
        Country of manufacture. Accepts "German", "Japanese", "Italian"
    """

    yearly_change = {"German": -0.05, "Japanese": -0.07, "Italian": 0.05}

    # Make sure input values are valid
    if country not in yearly_change:
        print("Value error: country must be \"German\", \"Japanese\", or \"Italian\"")
        return
    if not isinstance(purchase_price, int) or not isinstance(age, int):
        print("Value error: purchase_price and age must be integers")
        return

    return int(purchase_price * ((1 + yearly_change[country]) ** age))


def probs_1_thru_7():
    """All normal-credit problems for week 4."""


    # Problem 1

    # (function defined above)
    print(average(7, 5, 9))
    print(average(6, 6, 7))


    # Problem 2

    # The script will not run if the function is called before (above) its definition.


    # Problem 3

    # This will not work because num1 is only defined inside the average() function.
    # print(num1)


    # Problem 4

    print()
    for dog_age in [5, 11]:
        print(f"{dog_age} dog years is equivalent to {dog_to_human_years(dog_age)} human years.")


    # Problem 5

    print()
    country = "Italian"
    age = 10
    print(f"The value of your {country} car will be ${car_value(10_000, age, country):,} after {age} years.")


    # Problem 6

    print("\nDog's Age Calculator:")
    dog_name = input("What is your dog's name? ")
    dog_age = None
    while dog_age is None:
        dog_age = input(f"How old is {dog_name}? ")
        try:
            try:
                dog_age = int(dog_age)
            except ValueError:
                dog_age = float(dog_age)
        except ValueError:
            print("Please enter a number")
            dog_age = None
    human_years = dog_to_human_years(dog_age)

    if isinstance(human_years, int):
        human_years = f"{human_years:d}"
    elif isinstance(human_years, float):
        human_years = f"{human_years:.1f}"
    print(f"Your {dog_name} is {human_years} human years old")


    # Problem 7

    print("\nIce cream cone price calculator:")
    scoops = None
    while scoops is None:
        try:
            scoops = int(input("How many scoops would you like? "))
        except ValueError:
            print("Please enter an integer")

    price = cone_price(scoops)
    print(f"A {scoops:,}-scoop cone will cost ${price:,.2f}")


# Extra Credit


def download_data(url, container):
    """Downloads a csv file and puts it into the given mutable \"container\" (list, etc.)"""
    container[0] = pandas.read_csv(url)


def print_status(msg):
    """Prints a message without a newline so we can replace this text later using \\r."""
    print(msg, end='')
    sys.stdout.flush()


def download_with_status_msg(url, msg):
    """Download a csv file and print a status message if it's taking some time."""

    # Create a mutable object we can put the result of the download thread into,
    # since Thread.join() doesn't return the return value of its target function
    container = [None]

    downloader = Thread(target=download_data, args=[url, container])
    status_info = Timer(1.0, print_status, args=[msg])

    downloader.start()
    status_info.start()

    downloader.join()
    if status_info.is_alive():
        # Timer hasn't printed anything
        status_info.cancel()
    else:
        # Delete the status text
        sys.stdout.write("\r" + " "*len(msg) + "\r")
        sys.stdout.flush()

    # container[0] is the result of download_data() from the downloader thread
    return container[0]


def historic_cone_price(month, year, print_result=False):
    """Finds the average price of an ice-cream cone during a given month and year.

    Parameters
    ----------
    month : int or string
        Month of year for price lookup. Can be month name or number
    year : int
        Year of price lookup
    print_result : bool, optional
        If true, will print the result as a complete sentence

    Returns
    -------
    float or None
        Price in dollars or None if data for that month is missing or invalid
    """

    data = download_with_status_msg(
        "https://raw.githubusercontent.com/Mohaim-1/cs161/refs/heads/main/week04/ice-cream-prices.csv",
        "Downloading data file...")
    # Make it so each row can be easily referenced by year
    data.index = data["Year"].tolist()

    # Validate inputs and look up the cone price
    if isinstance(month, int):
        if month < 1 or month > 12:
            print("Value error: month is {month} but must be between 1 and 12")
            return
        price = data.loc[year].iloc[month]
        sep = "/"
    elif isinstance(month, str):
        formatted_month = month[:3].title()
        if formatted_month not in data.columns:
            print("Value error: \"{month}\" is not a valid month name")
            return
        price = data.loc[year][formatted_month]
        sep = " "
    else:
        print("Type error: month must be an int or string")
        return

    # Data may be missing so we need to validate the result
    if not isinstance(price, float):
        try:
            price = float(price)
        except ValueError as e:
            print(f"Data for {data.columns[month]} {year} is invalid: {e}")
            return

    if print_result:
        print(f"The average price of an ice cream cone during {month}{sep}{year} was ${price:.2f}")
    return price


probs_1_thru_7()
print()
historic_cone_price('April', 2018, True)


