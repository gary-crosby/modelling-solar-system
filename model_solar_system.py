'''
Description:

Program displays information about planets in our solar system. For each planet your program should hold its: 
* Name
* Mass
* Planet type (e.g., terrestrial, gas giant, dwarf planet)
* Distance from the Sun
* A list of the planet's permanently-named moons and a count of provisional moons

User can query the data by asking questions such as: 
* Tell me everything about Saturn? 
* How massive is Neptune? 
* Is Pluto in the list of planets? 
* How many moons does Earth have? 

Created by Gary Crosby as the Final Assessment project in
SHU MSc Computer Science module Fundamentals of Computing 
'''

# Standard library imports
import json;

# Import JSON file and convert to Python dictionary
#
# TO DO -- ADD ERROR HANDLING 
#
with open('solar_system_data.json') as json_file:
    solar_system = json.load(json_file)   
    print(solar_system)   # For debugging
    print(type(solar_system))  # For debugging
    print(solar_system['planets'])  # For debugging
    print(type(solar_system['planets']))  # For debugging
    print(solar_system['planets'][0])  # For debugging
    print(type(solar_system['planets'][0]))  # For debugging
    print(solar_system['planets'][0]['name'])  # For debugging
    print(type(solar_system['planets'][0]['name']))  # For debugging
    print(solar_system['planets'][0]['mass_kg'])  # For debugging
    print(type(solar_system['planets'][0]['mass_kg']))  # For debugging
    print(solar_system['planets'][0]['type'])  # For debugging
    print(type(solar_system['planets'][0]['type']))  # For
    print(solar_system['planets'][0]['distance_from_sun_km'])  # For debugging
    print(type(solar_system['planets'][0]['distance_from_sun_km']))
    print(solar_system['planets'][0]['moons'])  # For debugging
    print(type(solar_system['planets'][0]['moons']))  # For debugging
    print(solar_system['planets'][0]['moons']['permanently_named']) 
    print(type(solar_system['planets'][0]['moons']['permanently_named']))  # For debugging
    print(solar_system['planets'][0]['moons']['provisional_count'])
    print(type(solar_system['planets'][0]['moons']['provisional_count']))  # For debugging  
    
