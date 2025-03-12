# Katie Fournier
# CS 161 Winter 2025
# Week 9


from typing import Union

# for locale-aware thousands separator
import locale
locale.setlocale(locale.LC_ALL, '')


class Student:
    """A grade-school student.

    Attributes:
        first_name (str): the student's name
        age (int): the student's age
        grade (Union[int, str]): the student's grade year, usually 1-12 or 'K'
    """

    def __init__(self, first_name: str, age: int, grade: Union[int, str]):
        self.first_name = first_name
        self.age = age
        self.grade = grade

    @staticmethod
    def with_ordinal_indicator(number: int) -> str:
        """Returns the number with its ordinal indicator (e.g. 2 -> '2nd')."""

        if number % 10 in ([0] + list(range(4, 10))) or number % 100 in [11, 12, 13]:
            suffix = 'th'
        else:
            suffix = ['st', 'nd', 'rd'][(number % 10) - 1]
        return str(number) + suffix

    def __repr__(self):
        # if self.grade is a positive integer make it pretty
        if isinstance(self.grade, int) and self.grade >= 1:
            grade_str = self.with_ordinal_indicator(self.grade)
        else:
            grade_str = self.grade

        attributes = {'Name':self.first_name, 'Age':self.age, 'Grade':grade_str}
        return '\n'.join([f"{key}: {attributes[key]}" for key in attributes.keys()])


class Staff:
    """An employee at an organization.

    Parameters:
        first_name (str): employee's first name
        department (str): the department they work in
        role (str): their role in the organization
        salary (Union[int, float]): dollars per year
    """

    def __init__(self, first_name: str, department: str, role: str, salary: Union[int, float]):
        self.first_name = first_name
        self.department = department
        self.role = role
        self.salary = salary

    def __repr__(self):
        attributes = {'Name':self.first_name, 'Role':self.role, 'Department':self.department}
        return '\n'.join([f"{key}: {attributes[key]}" for key in attributes])


class Teacher(Staff):
    """A teacher at an organization.

    Parameters:
        first_name (str): their first name
        department (str): the department they work in
        salary (Union[int, float]): dollars per year
        age (int): years
    """

    def __init__(self, first_name: str, department: str, salary: Union[int, float], age: Union[int, float]):
        self.role = 'Teacher'
        super().__init__(first_name, department, self.role, salary)
        self.age = age

    def __repr__(self):
        attributes = {'Name':self.first_name, 'Age':self.age, 'Role':self.role, 'Department':self.department}
        return '\n'.join([f"{key}: {attributes[key]}" for key in attributes.keys()])


class Square:
    """A polygon with four equilateral sides."""

    def __init__(self, side_length: Union[int, float]):
        self.side_length = side_length

    def area(self) -> Union[int, float]:
        """Returns the area of the square."""
        return self.side_length**2

    def perimeter(self) -> Union[int, float]:
        """Returns the perimeter of the square."""
        return self.side_length * 4


# Will not execute if the script is used as a library
if __name__ == '__main__':

    # Problem 1
    raj = Student('Raj', 16, 11)
    joe = Student('Joe', 17, 11)
    print(raj)
    print(joe)
    print()

    # Problem 2
    raj = Teacher('Raj', 'Science', 10_000, 20)
    joe = Teacher('Joe', 'Science', 20_000, 58)
    print(raj)
    print(joe)
    print()

    # Problem 3
    square1 = Square(10)
    square2 = Square(20)
    objects = {'square1': square1, 'square2': square2}
    for name in objects:
        print(f"The Area of {name} is: {objects[name].area()}\n"
              f"The Perimeter of {name} is: {objects[name].perimeter()}")


