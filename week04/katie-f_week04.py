# Katie Fournier
# Cs 161 Week 04

def probs_1_thru_7():
    """Contains all normal-credit assigned problems for week 4"""

    def average(num1, num2, num3):
        """Finds the average of three numbers."""
        return (num1 + num2 + num3)/3

    print(average(7, 5, 9))
    print(average(6, 6, 7))
    # The script will not run if the function is called before (above) its definition.

    # This will not work because num1 is only defined inside the average() function.
    # print(num1)

    def dog_to_human_years(dog_age) -> int:
        """Converts a dog's age in years to human years."""
        return 24 + (dog_age - 2) * 4

    for dog_age in [5, 11]:
        print(f"{dog_age} dog years is equivalent to {dog_to_human_years(dog_age)} human years.")

    def car_value(purchase_price, age, country) -> int:
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
            raise ValueError
        if not isinstance(purchase_price, int) or not isinstance(age, int):
            raise TypeError

        return int(purchase_price * ((1 + yearly_change[country]) ** age))

    country = "Italian"
    age = 10
    print(f"The value of your {country} car will be ${car_value(10_000, age, country):,} after {age} years.")

    def ice_cream_cone_price(scoops):
        """Returns the cost of an ice cream cone in dollars."""
        return scoops * 1.15 + 2.25

    print("\nIce cream cone price calculator:")
    scoops = int(input("How many scoops would you like? "))
    print(f"A {scoops}-scoop cone will cost ${ice_cream_cone_price(scoops):.2f}")

def historical_ice_cream_price(year) -> float:
    import pandas

    data = pandas.read_csv("http://website.com/file.csv")


# probs_1_thru_7()

