# Katherine Fournier
# CS 161, Week 1


# Problem 1

pet_type = "dog"
pet_name = "Duke"
print(f"I have a {pet_type} and their name is {pet_name}.")


# Problem 2

def problem2():
    print("Enter your first name: ", end="")
    name = input()

    # These input values must be valid numbers since we'll do math with them later
    age = prompt_int("Enter your current age: ")
    yearly_savings = prompt_int("Enter your yearly savings: ")

    print((f"Hello {name}! You are currently {age} years old.\n"
           f"In 10 years, you will be {age+10} years old.\n"
           f"If you save ${yearly_savings} each year, in 5 years you will have saved ${yearly_savings*5}.\n"
           f"Your average monthly savings is ${yearly_savings/12:.2f}."))

# Repeats prompt until the user enters an integer
def prompt_int(prompt) -> int:
    number = None
    while number == None:
        print(prompt, end="")
        try:
            number = int(input())
        except ValueError:
            print("Please enter a whole number.")
    return number

problem2()


# Problem 3
