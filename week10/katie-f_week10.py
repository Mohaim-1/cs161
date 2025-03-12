# Katie Fournier
# CS 161 Winter 2025
# Week 10


from math import ceil
from typing import Union


class SolarObject:
    """An object in our solar system that is orbiting something else.

    Attributes:
        apoapsis (Union[int, float]): farthest point in the object's orbit in AU
        orbital_period (Union[int, float]): days to complete one orbit around its primary body
        spin (str): description of the object's spin
    """
        
    def __init__(self, apoapsis: Union[int, float], orbital_period_days: Union[int, float], spin: str):
        self.apoapsis = apoapsis
        self.orbital_period = orbital_period_days
        self.spin = spin
        self.orbit_time_unit = 'days'

    def colonization(self) -> int:
        """Estimates the potential colonization population (in billions) of the object.

        The estimate is based on Earth's population and the object's farthest distance from its
        primary body (apoapsis) relative to Earth's average distance from the sun (1 AU).

        The formula used is:
            object's population = ⌈ Earth's population / object's apoapsis ⌉
        """
        return ceil(6 / self.apoapsis)

    def __repr__(self):
        return (f"{self.apoapsis}  au from the sun, spins  {self.spin}  "
                f"and has an orbit taking  {self.orbital_period}  {self.orbit_time_unit} "
                f"and can support a population of :  {self.colonization()}  billion")

    def spin(self):
        pass


class Planet(SolarObject):
    """A planet orbiting the sun.

    Attributes:
        apoapsis (Union[int, float]): farthest point in the object's orbit in AU
        orbital_period (Union[int, float]): days to complete one orbit around the sun
    """

    def __init__(self, apoapsis: Union[int, float], orbital_period: Union[int, float]):
        super().__init__(apoapsis, orbital_period, "slightly elliptical")


class Comet(SolarObject):
    """A comet orbiting the sun.

    Attributes:
        apoapsis (Union[int, float]): farthest distance from the sun in AU
        orbital_period (Union[int, float]): years to complete one orbit around the sun
    """

    def __init__(self, apoapsis: Union[int, float], orbital_period: Union[int, float]):
        super().__init__(apoapsis, orbital_period, "like crazy")
        self.orbit_time_unit = 'years'


# Orbital data from Wikipedia
orbital_bodies = {'Halley': Comet(35.12, 74.7),
                  'HaleBopp': Comet(354, 2399),
                  'Earth': Planet(1.0167, 365.256),
                  'Mars': Planet(1.6660, 687.0)}

for orbital_body in orbital_bodies:
    print(f"{orbital_body}  is  {orbital_bodies[orbital_body]}")

