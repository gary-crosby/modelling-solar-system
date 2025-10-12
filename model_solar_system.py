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
import json
from pathlib import Path

# Class definitions
class Planet:
    def __init__(self, name, mass_kg, type, orbit_km, orbit_yr, moons_perm=[], moons_prov=0):
        self.name = name
        self.mass_gigatons = float(mass_kg/1000000000000) # convert kg to billions of tons
        self.type = type
        self.orbit_megakms = float(orbit_km/1000000) # convert km to millions of km
        self.orbit_yr = orbit_yr
        # avoid mutable default argument
        self.moons_perm = moons_perm or []
        self.moons_prov_n = moons_prov

class DataSource:
    def __init__(self, name, url):
        self.name = name
        self.url = url  
    
# Import JSON file and convert to Python dictionary
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


# Create list of Planet objects from JSON data
def create_planet(planet_data):
    """Create and return a Planet object from a single planet dict from the JSON."""
    name = planet_data.get('name')
    type = planet_data.get('type')
    orbit_megakms = planet_data.get('distance_from_sun_km')
    orbit_yr = planet_data.get('orb_yr')
    mass_gigatons = planet_data.get('mass_kg')
    moons_info = planet_data.get('moons', {}) #monns_info is not a field in JSON or a Planet.property
    moons_perm_list = moons_info.get('permanently_named', [])
    moons_prov_n = moons_info.get('provisional_count', 0)
    p = Planet(name, mass_gigatons, type, orbit_megakms, orbit_yr, list(moons_perm_list), moons_prov_n)
    return p

# Main program
planets_dict = getJSON()
if planets_dict is None:
    # getJSON already printed a helpful error message so we can exit the program
    raise SystemExit(1)

# Create a list of planet instances
#print('-----') # debug only
planets = []
for planet_data in planets_dict.get('planets', []):
    planet = create_planet(planet_data)
    planets.append(planet)
# Print out details of each planet
    print(planet.name) # debug only
    print('  mass_gigatons:', planet.mass_gigatons) # debug only
    print('  type:', planet.type) # debug only
    print('  orbit_megakms:', planet.orbit_megakms) # debug only
    print('  orbit_yr:', planet.orbit_yr) # debug only
    print('  moons_perm:', planet.moons_perm) # debug only
    print('  moons_prov_n:', planet.moons_prov_n) # debug only
    print('-----') # debug only

# Setup GUI
