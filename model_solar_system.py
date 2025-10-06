'''
Description:

Program displays information about planets in our solar system. For each planet your program should hold its: 
* Name
* Mass (kg)
* Planet type (e.g., terrestrial, gas giant, dwarf planet)
* Distance from the Sun (km)
* Orbital period (earth years)
* A list of the planet's permanently-named moons, if any
* A count of provisional moons, if any

User can query the data by asking questions such as: 
* Tell me everything about Saturn? 
* How massive is Neptune? 
* Is Pluto in the list of planets? 
* How many moons does Earth have? 

Created by Gary Crosby as the Final Assessment project in
SHU MSc Computer Science module 'Fundamentals of Computing' 
'''

# Standard library imports
import json;

# Class definitions
class Planet:
    def __init__(self, name, mass_kg, planet_type, distance_from_sun_km, orb_yr, moons_perm = [], moons_prov = 0 ):
        self.name = name
        self.mass_kg = mass_kg
        self.type = planet_type
        self.orbit_km = distance_from_sun_km
        self.orbit_yr = orb_yr
        self.moons_perm = moons_perm
        self.moons_prov_n = moons_prov

class MoonPerm:
    def __init__(self, name):
        self.name = name

class DataSource:
    def __init__(self, name, url):
        self.name = name
        self.url = url  
    
# Import JSON file and convert to Python dictionary
try:
    with open('solar_system_data.json') as json_file:
        solar_system = json.load(json_file)   
except:
    print("Error reading JSON file.")


