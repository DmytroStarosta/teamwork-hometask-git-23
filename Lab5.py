"""
Import module statistics
Import enum from Enum
Created class "Type" to show how it works 
Created class "Planet" with planets parameters
"""
import statistics
from enum import Enum

class Type(Enum):
    """
    Represents the type of a planet
    """
    TERRESTRIAL = 1
    JOVIAN = 2

class Planet:
    """
    Represents the attributes of the planets of the solar system
    """
    # pylint: disable=R0913
    def __init__ (self, name, mass_in_kg, orbital_velocity, mean_temperature, length_of_day, \
                   distance_from_sun):
        """ 
        A constructor that initializes the object's attributes
        """
        self.__name = name
        self.__mass_in_kg = mass_in_kg
        self.__orbital_velocity = orbital_velocity
        self.__mean_temperature = mean_temperature
        self.__length_of_day = length_of_day
        self.__distance_from_sun = distance_from_sun

    @property
    def name(self):
        """
        Displays the attribute name
        """
        return self.__name
    @name.setter
    def name(self, value):
        """
        Sets the value to name
        """
        self.__name = value
    @name.deleter
    def name(self):
        """
        delete attribute name
        """
        del self.__name

    @property
    def mass_in_kg(self):
        """
        Displays the attribute mass_in_kg
        """
        return self.__mass_in_kg
    @mass_in_kg.setter
    def mass_in_kg(self, value):
        """
        Sets the value to mass_in_kg
        """
        self.__mass_in_kg = value
    @mass_in_kg.deleter
    def mass_in_kg(self):
        """
        delete attribute mass_in_kg
        """
        del self.__mass_in_kg

    @property
    def orbital_velocity(self):
        """
        Displays the attribute orbital_velocity
        """
        return self.__orbital_velocity
    @orbital_velocity.setter
    def orbital_velocity(self, value):
        """
        Sets the value to orbital_velocity
        """
        self.__orbital_velocity = value
    @orbital_velocity.deleter
    def orbital_velocity(self):
        """
        delete attribute orbital_velocity
        """
        del self.__orbital_velocity

    @property
    def mean_temperature(self):
        """
        Displays the attribute mean_temperature
        """
        return self.__mean_temperature
    @mean_temperature.setter
    def mean_temperature(self, value):
        """
        Sets the value to mean_temperature
        """
        self.__mean_temperature = value
    @mean_temperature.deleter
    def mean_temperature(self):
        """
        delete attribute mean_temperature
        """
        del self.__mean_temperature

    @property
    def length_of_day(self):
        """
        Displays the attribute length_of_day
        """
        return self.__length_of_day
    @length_of_day.setter
    def length_of_day(self, value):
        """
        Sets the value to length_of_day
        """
        self.__length_of_day = value
    @length_of_day.deleter
    def length_of_day(self):
        """
        delete attribute length_of_day
        """
        del self.__length_of_day

    @property
    def distance_from_sun(self):
        """
        Displays the attribute distance_from_sun
        """
        return self.__distance_from_sun
    @distance_from_sun.setter
    def distance_from_sun(self, value):
        """
        Sets the value to distance_from_sun
        """
        self.__distance_from_sun = value
    @distance_from_sun.deleter
    def distance_from_sun(self):
        """
        delete attribute distance_from_sun
        """
        del self.__distance_from_sun
    def __str__(self):
        """
        returns a string representation of the object
        """
        return f"Planet {self.__name}, has the following parameters: mass {self.__mass_in_kg}," \
               f"orbital velocity {self.__orbital_velocity}," \
               f"temperature {self.__mean_temperature}," \
               f"length of day {self.__length_of_day}" \
               f"and distance from sun {self.__distance_from_sun}" 

    def __repr__(self):
        """
        returns representation of the object, that can be used to restore the object
        """
        return f"Planet {self.__name},  mass: {self.__mass_in_kg}," \
               f"orbital velocity: {self.__orbital_velocity}," \
               f"temperature: {self.__mean_temperature}," \
               f"length of day: {self.__length_of_day}," \
               f"distance from sun: {self.__distance_from_sun} "

class Planetary:
    """
    Represents addition, sorting and other operations on objects
    """
    def __init__(self):
        self.planets = []

    def add_planets(self, planet):
        """
        Addition method
        """
        self.planets.append(planet)

    def remove_planets(self, planet):
        """
        Removal method
        """
        self.planets.remove(planet)

    def sort_by_length_of_day(self):
        """
        Sorting method
        """
        return self.planets.sort(key=lambda x: x.length_of_day, reverse = True)

    def find_distance_between(self, planet_a, planet_b):
        """
        Distance finding method
        """
        distance = abs(planet_a.distance_from_sun - planet_b.distance_from_sun)
        return distance

    def find_average_mass(self):
        """
        Avarage mass finding method
        """
        average_mass = [planet.mass_in_kg for planet in self.planets]
        return statistics.mean(average_mass)

if __name__  == "__main__":
    planetary_system = Planetary()

    print("")
    print("Enum demonstration:")
    a = Type.TERRESTRIAL
    b = Type.JOVIAN
    print(a, b)

    mercury = Planet("Mercury", 3.285e23, 47360, 350, 58.6, 57.9e6)
    venus = Planet("Venus", 4.867e24, 35020, 464, 116.8, 108.2e6)
    earth = Planet("Earth", 5.972e24, 29780, 15, 24, 149.6e6)
    mars = Planet("Mars", 6.39e23, 24100, -65, 25, 227.9e6)
    jupiter = Planet("Jupiter", 1.898e27, 13170, -110, 10, 778.5e6)
    saturn = Planet("Saturn", 5.683e26, 9640, -140, 10.7, 1.4e9)
    uranus = Planet("Uranus", 8.681e25, 6810, -195, 17.2, 2.9e9)
    neptune = Planet("Neptune", 1.024e26, 5430, -200, 16.1, 4.5e9)

    planetary_system.add_planets(mercury)
    planetary_system.add_planets(venus)
    planetary_system.add_planets(earth)
    planetary_system.add_planets(mars)
    planetary_system.add_planets(jupiter)
    planetary_system.add_planets(saturn)
    planetary_system.add_planets(uranus)
    planetary_system.add_planets(neptune)

    planet_1 = Planet("Earth", 972e24, 29780, 15, 24, 149.6e6)
    planet_2 = Planet("Venus", 4.867e24, 35020, 464, 116.8, 108.2e6)

    print("")
    planetary_system.sort_by_length_of_day()
    for planet_1 in planetary_system.planets:
        print(planet_1)
        print("")
        print("Repr demonstration:")
        print(repr(planet_1))
        print("")
        print("")
    distance_between_planets = planetary_system.find_distance_between(planet_1, planet_2)
    planet_name_a = planet_1.name
    planet_name_b = planet_1.name
    print(f"Distance between {planet_name_a} and {planet_name_b}: {distance_between_planets} km")
    print("")
    average_mass_result = planetary_system.find_average_mass()
    print(f"The average mass of the given planets: {average_mass_result} kg")
