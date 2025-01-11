# Katie Fournier
# CS 161, Week 1

def problem1():
    """Print the name of my pet."""
    pet_type = "dog"
    pet_name = "Duke"
    print(f"I have a {pet_type} and their name is {pet_name}.")

def problem2():
    """Prompt the user for their personal info then print some data based on that."""

    print("Enter your first name: ", end="")
    name = input()

    # These input values must be valid numbers since we'll do math with them later
    # input_int() will always return an integer
    age = -1
    while age < 0:
        age = input_int("Enter your current age: ")
        if age < 0:
            print("That is unlikely.")
    yearly_savings = input_int("Enter your yearly savings: ")

    print((f"Hello {name}! You are currently {age} years old.\n"
           f"In 10 years, you will be {age+10} years old.\n"
           f"If you save ${yearly_savings} each year, in 5 years you will have saved ${yearly_savings*5}.\n"
           f"Your average monthly savings is ${yearly_savings/12:.2f}."))

def problem3():
    """Print the number of seconds in this month."""
    from datetime import datetime

    today = datetime.today()
    this_month = datetime(year=today.year, month=today.month, day=1)
    # Determine next month, accounting for current month being December
    if today.month < 12:
        next_month = datetime(year=today.year, month=today.month+1, day=1)
    else:
        next_month = datetime(year=today.year+1, month=1, day=1)

    month_seconds = (next_month - this_month).total_seconds()
    month_name = today.strftime("%B")
    print(f"The number of seconds in {month_name} is {month_seconds:.0f}")

def problem4():
    """Prints how many dozens of eggs from an input number."""
    eggs = -1
    while eggs < 0:
        eggs = input_int("Enter the number of eggs: ")
        if eggs < 0:
            print("Egg debt is beyond the scope of this program.")
    print(f"This makes {eggs // 12} dozen eggs with {eggs % 12} left over")

def input_int(prompt) -> int:
    """Repeats a prompt until the user enters an integer."""

    number = None
    # "number" will have a value once the input value can be cast to an int
    while number is None:
        print(prompt, end="")
        try:
            number = int(input())
        except ValueError:
            print("Please enter a whole number.")
    return number

problem1()
problem2()
problem3()
problem4()