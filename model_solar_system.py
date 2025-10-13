'''
Program Description:

Program displays information about all recocnized planets in our solar system.
For each planet your program should hold its: 
* Name
* Mass (earth mass)
* Planet type (e.g., terrestrial, gas giant, dwarf planet)
* Distance from the Sun (AU where 1 AU == 149,597,870.7 km)
* Orbital period (earth years)
* A list of the planet's permanently-named moons, if any
* A count of provisional moons, if any

User can query the data by asking questions such as: 
* Tell me everything about Saturn? 
* How massive is Neptune? 
* Is Pluto in the list of planets? 
* How many moons does Earth have? 

Additional notes:
* The number of decimal places for mass relative to Earth and distance from the Sun in AU have been chosen to provide useful precision without excessive detail.
* The number of permanently named moons and provisional moons varies with the data source and date. The data used were accurate as of mid-2025.

Created by Gary Crosby as the Final Assessment project in SHU online MSc Computer Science module 'Fundamentals of Computing' 
'''

# Standard library imports
import json
from pathlib import Path
import tkinter as tk

# Class definitions
class Planet:
    def __init__(self, name, mass_kg, type, orbit_km, orbit_yr, moons_perm=None, moons_prov=0, mass_earth=0, orbit_au=0):
        # # # # # # # #  -- TO DO -- # # # # # #
        # Add docstring
        self.name = name
        self.mass_kg = mass_kg
        self.type = type
        self.orbit_au = round((float(orbit_km/149597870.7)),2) 
        self.orbit_yr = orbit_yr
        self.moons_perm = list(moons_perm) if moons_perm is not None else [] # avoid mutable default argument
        self.moons_prov_n = moons_prov
        self.mass_earth = mass_earth # mass relative to Earth

class Reference:
    # # # # # # # #  -- TO DO -- # # # # # #
    # Add docstring
    def __init__(self, name, url):
        self.name = name
        self.url = url  

# Function definitions

def getJSON():
    """Load the JSON file located in the same folder as this script and return the dict.

    Returns None on failure and prints an error message with details.
    """
    base = Path(__file__).parent
    json_path = base / 'solar_system_data.json'
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            planets_dict = json.load(json_file)
            return planets_dict
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Unexpected error reading JSON: {e}")

def create_planet(planet_data):
    """Create and return a Planet object from a single planet dict from the JSON."""
    name = planet_data.get('name')
    type = planet_data.get('type')
    orbit_km = planet_data.get('distance_from_sun_km')
    orbit_yr = planet_data.get('orb_yr')
    mass_kg = planet_data.get('mass_kg')
    moons_info = planet_data.get('moons', {}) #moons_info is not a field in JSON or a Planet.property
    moons_perm_list = moons_info.get('permanently_named', [])
    moons_prov_n = moons_info.get('provisional_count', 0)
    p = Planet(name, mass_kg, type, orbit_km, orbit_yr, list(moons_perm_list), moons_prov_n,mass_earth=0, orbit_au=0)
    return p

def create_reference(ref_data):
    """Create and return a References object from a single reference dict from the JSON."""
    name = ref_data.get('name')
    url = ref_data.get('url')
    r = Reference(name, url)
    return r

# Main program

# Load JSON data
planets_dict = getJSON()
if planets_dict is None:
    # getJSON already printed a helpful error message so we can exit the program
    raise SystemExit(1)

# Create a list of planet instances
#print('-----') # debug only
planets = []
earth_mass_kg = 0
for planet_data in planets_dict.get('planets', []):
    planet = create_planet(planet_data)
    planets.append(planet) 
    # Get earth mass in kg for later calculations
    if planet.name.lower() == 'earth':
        earth_mass_kg = planet.mass_kg  
        # print('earth_mass_kg:', earth_mass_kg) # debug only
    # Print out details of each planet # debug only
    # print(planet.name) # debug only
    # print('  mass_kg:', planet.mass_kg) # debug only
    # print('  type:', planet.type) # debug only
    # print('  orbit_au:', planet.orbit_au) # debug only
    # print('  orbit_yr:', planet.orbit_yr) # debug only
    # print('  moons_perm:', planet.moons_perm) # debug only
    # print('  moons_prov_n:', planet.moons_prov_n) # debug only
    # print('-----') # debug only

# Sort planets list by planet distance from sun, ascending order
planets.sort(key=lambda p: p.orbit_au)   
# print('Planets sorted by distance from Sun (AU):') # debug only
# for planet in planets:
#     print(f"{planet.name}: {planet.orbit_au} AU") # debug only

# For each planet calculate its earth mass and set the property
# Use 4 decimal places because dwarf planets have very small mass relative to Earth
for planet in planets:    
    planet.mass_earth = round((planet.mass_kg / earth_mass_kg), 4) 
    # print('mass_earth:', planet.mass_earth) # debug only
    # print('-----') # debug only   

# Create a list of references (i.e., data sources)
references = []
for ref_data in planets_dict.get('references', []):
    reference = create_reference(ref_data)
    references.append(reference)
    # Print out details of each reference # debug only
    # print('Reference Name:', reference.name) # debug only     
    # print('Reference URL:', reference.url) # debug only

# Create GUI using tkinter
# # # # # # # #  -- TO DO -- # # # # # #

