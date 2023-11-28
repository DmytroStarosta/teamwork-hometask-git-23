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
    def __init__ (self, name , mass_in_kg, orbital_velocity, mean_temperature, length_of_day, distance_from_sun ):
        self.__name = name
        self.__mass_in_kg = mass_in_kg
        self.__orbital_velocity = orbital_velocity
        self.__mean_temperature = mean_temperature
        self.__length_of_day = length_of_day
        self.__distance_from_sun = distance_from_sun 

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @name.deleter
    def name(self):
        del self.__name

    @property
    def mass_in_kg(self):
        return self.__mass_in_kg
    @mass_in_kg.setter
    def mass_in_kg(self, value):
        self.__mass_in_kg = value
    @mass_in_kg.deleter
    def mass_in_kg(self):
        del self.__mass_in_kg

    @property
    def orbital_velocity(self):
        return self.__orbital_velocity
    @orbital_velocity.setter
    def orbital_velocity(self, value):
        self.__orbital_velocity = value
    @orbital_velocity.deleter
    def orbital_velocity(self):
        del self.__orbital_velocity

    @property
    def mean_temperature(self):
        return self.__mean_temperature
    @mean_temperature.setter
    def mean_temperature(self, value):
        self.__mean_temperature = value
    @mean_temperature.deleter
    def mean_temperature(self):
        del self.__mean_temperature

    @property
    def length_of_day(self):
        return self.__length_of_day
    @length_of_day.setter
    def length_of_day(self, value):
        self.__length_of_day = value
    @length_of_day.deleter
    def length_of_day(self):
        del self.__length_of_day

    @property
    def distance_from_sun(self):
        return self.__distance_from_sun
    @distance_from_sun.setter
    def distance_from_sun(self, value):
        self.__distance_from_sun = value
    @distance_from_sun.deleter
    def distance_from_sun(self):
        del self.__distance_from_sun
        
    def __str__(self):
        return f"Planet {self.__name}, has the following parameters: mass {self.__mass_in_kg}, orbital velocity {self.__orbital_velocity}, temperature {self.__mean_temperature}, length of day {self.__length_of_day} and distance from sun {self.__distance_from_sun} "
    
    def __repr__(self):
        return f"Planet {self.__name},  mass: {self.__mass_in_kg}, orbital velocity: {self.__orbital_velocity}, temperature: {self.__mean_temperature}, length of day: {self.__length_of_day}, distance from sun: {self.__distance_from_sun} "

class Planetary:
    """
     Represents addition, sorting and other operations on objects
    """ 
    def __init__(self):
        self.planets = []

    def add_planets(self, planet):
        self.planets.append(planet)
    
    def remove_planets(self, planet):
        self.planets.remove(planet)

    def sort_by_length_of_day(self):
        return self.planets.sort(key=lambda x: x.length_of_day, reverse = True)
    
    def find_distance_between(self, planetA, planetB):
        distance = abs(planetA.distance_from_sun - planetB.distance_from_sun)
        return distance
      
    def find_average_mass(self):
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

    planetA = Planet("Earth", 972e24, 29780, 15, 24, 149.6e6)
    planetB = Planet("Venus", 4.867e24, 35020, 464, 116.8, 108.2e6)

    print("")
    planetary_system.sort_by_length_of_day()
    for planet in planetary_system.planets:
        print(planet)
        print("")
        print("Repr demonstration:")
        print(repr(planet))
        print("")
        print("")
    
    distance = planetary_system.find_distance_between(planetA, planetB)
    planet_name_a = planetA.name
    planet_name_b = planetB.name
    print(f"Distance between {planet_name_a} and {planet_name_b}: {distance} km")
    print("")
    average_mass = planetary_system.find_average_mass()
    print(f"The average mass of the given planets: {average_mass} kg")
    print("")