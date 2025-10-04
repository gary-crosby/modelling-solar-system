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
    def __init__(self, name, mass_tons, planet_type, distance_from_sun_km, orb_yrs, moons_perm = [], moons_prov = 0 ):
        self.name = name
        self.mass_tons = mass_tons
        self.type = planet_type
        self.orbit_kms = distance_from_sun_km
        self.orbit_yrs = orb_yrs
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
        # print(solar_system)   # For debugging
        # print(type(solar_system))  # For debugging
        # print(solar_system['planets'])  # For debugging
        # print(type(solar_system['planets']))  # For debugging
        # print(solar_system['planets'][0])  # For debugging
        # print(type(solar_system['planets'][0]))  # For debugging
        # print(solar_system['planets'][0]['name'])  # For debugging
        # print(type(solar_system['planets'][0]['name']))  # For debugging
        # print(solar_system['planets'][0]['mass_kg'])  # For debugging
        # print(type(solar_system['planets'][0]['mass_kg']))  # For debugging
        # print(solar_system['planets'][0]['type'])  # For debugging
        # print(type(solar_system['planets'][0]['type']))  # For
        # print(solar_system['planets'][0]['distance_from_sun_km'])  # For debugging
        # print(type(solar_system['planets'][0]['distance_from_sun_km']))
        # print(solar_system['planets'][0]['orb_yrs'])  # For debugging
        # print(type(solar_system['planets'][0]['orb_yrs']))  # For debugging
        # print(solar_system['planets'][0]['moons'])  # For debugging
        # print(type(solar_system['planets'][0]['moons']))  # For debugging
        # print(solar_system['planets'][0]['moons']['permanently_named']) 
        # print(type(solar_system['planets'][0]['moons']['permanently_named']))  # For debugging
        # print(solar_system['planets'][0]['moons']['provisional_count'])
        # print(type(solar_system['planets'][0]['moons']['provisional_count']))  # For debugging
        # print(solar_system['data_sources'])  # For debugging
        # print(type(solar_system['data_sources']))  # For debugging                    
        # print(solar_system['data_sources'][0])  # For debugging
        # print(type(solar_system['data_sources'][0]))  # For debugging
        # print(solar_system['data_sources'][0]['name'])  # For debugging
        # print(type(solar_system['data_sources'][0]['name']))  # For debugging
        # print(solar_system['data_sources'][0]['url'])  # For debugging
        # print(type(solar_system['data_sources'][0]['url']))  # For debugging  
except:
    print("Error reading JSON file.");


