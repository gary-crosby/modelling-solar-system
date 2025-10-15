"""
Program Description:

Program displays information about all recocnized planets in our solar system.
For each planet your program should hold its: 
* Name
* Mass (relative to Earth's mass)
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
* Reads all data from solar_system_data.json which must be in the same folder as this script

Created by Gary Crosby for as the Final Assessment project in SHU's online MSc Computer Science module 'Fundamentals of Computing' 
"""

########## Setup ##########
 
# Standard library imports

import json
from pathlib import Path
import tkinter as tk

# Class definitions

class Planet:
    def __init__(self, name, mass_kg, type, orbit_km, orbit_yr, moons_perm=None, moons_prov=0, mass_earth=0, orbit_au=0):
        """ Initialize a Planet instance.
            mass_earth is mass relative to Earth and is set after planet is made. """
        self.name = name
        self.mass_kg = mass_kg
        self.type = type
        self.orbit_au = round((float(orbit_km/149597870.7)),2) 
        self.orbit_yr = orbit_yr
        self.moons_perm = list(moons_perm) if moons_perm is not None else [] # avoid mutable default argument
        self.moons_prov_n = moons_prov
        self.mass_earth = mass_earth # mass relative to Earth

    def set_mass_earth(self, earth_mass_kg):
        """ Calculate and set the mass_earth which is planet mass relative to Earth's mass.
            Use 4 decimal places because dwarf planets are  very small relative to Earth."""
        self.mass_earth = round((self.mass_kg / earth_mass_kg), 4)

class Reference:
    """ Initialize a Reference instance."""
    def __init__(self, name, url):
        self.name = name
        self.url = url  

# Function definitions

def getJSON():
    """ Load the JSON file located in the same folder as this script and return the dict.
        Returns None on failure and prints an error message with details."""
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
    """ Create and return a Planet object from a single planet dict from the JSON."""
    name = planet_data.get('name')
    type = planet_data.get('type')
    orbit_km = planet_data.get('distance_from_sun_km')
    orbit_yr = planet_data.get('orb_yr')
    mass_kg = planet_data.get('mass_kg')
    moons_info = planet_data.get('moons', {}) 
    moons_perm_list = moons_info.get('permanently_named', [])
    moons_prov_n = moons_info.get('provisional_count', 0)
    p = Planet(name, mass_kg, type, orbit_km, orbit_yr, list(moons_perm_list), moons_prov_n,mass_earth=0, orbit_au=0)
    return p

def create_reference(ref_data):
    """ Create and return a References object from a single reference dict from the JSON."""
    name = ref_data.get('name')
    url = ref_data.get('url')
    r = Reference(name, url)
    return r

def display_planet_info():
    ''' Display planet(s) information based on selected characteristic(s) '''
    text_area.delete(1.0, tk.END)  # Clear existing text
    for planet in planets:
        if not planet_vars[planet.name].get():
            continue  # Skip this planet if not selected
        info = f"{planet.name}\n"
        if mass_var.get():
            info += f"Mass: {planet.mass_earth} Earth masses\n"
        if type_var.get():
            info += f"Type: {planet.type}\n"  
        if orbit_au_var.get():
            info += f"Distance from sun: {planet.orbit_au} AU\n"
        if orbit_yr_var.get():
            info += f"Orbital period: {planet.orbit_yr} Earth years\n"
        if moons_var.get():
            info += f"Permanently named moons: {', '.join(planet.moons_perm) if planet.moons_perm else 'None'}\n"
            info += f"Provisional moons count: {planet.moons_prov_n}\n"

        info += "\n"

        ###### TO DO - Add references at the end of text_area #####

        text_area.insert(tk.END, info)

###### TO DO -- Add 'Select All' functionality for planets and properties ######
#def on_checkbox_toggle():

########## Main Program ########## 

# Load JSON data
planets_dict = getJSON()
if planets_dict is None:
    # getJSON already printed a helpful error message so we can exit the program
    raise SystemExit(1)

# Create a list of planet instances
planets = []
earth_mass_kg = 0
for planet_data in planets_dict.get('planets', []):
    planet = create_planet(planet_data)
    planets.append(planet)
    # Could use a known value for Earth's but its more elegant to get it from JSON data
    if planet.name.lower() == 'earth':
        earth_mass_kg = planet.mass_kg  

# For each planet set its earth_mass property
for planet in planets:    
    planet.set_mass_earth(earth_mass_kg)    

# Sort planets list by planet's distance from sun in ascending order
planets.sort(key=lambda p: p.orbit_au)   

# Create a list of references (i.e., data sources)
references = []
for ref_data in planets_dict.get('references', []):
    reference = create_reference(ref_data)
    references.append(reference)

# Create GUI using tkinter using default settings for fonts, colors etc.

# Basic window setup
root = tk.Tk()
root.title("Solar System Planets Explorer")
root.geometry("750x500") # Should fit on monitors as small as 800x600    
root.resizable(False, False)

 # Main frame
main = tk.Frame(root, padx=10, pady=10)
main.pack(expand=True, fill='both')

###### TO DO -- Add text Headings for 'Planets' and 'Characteristics' ######

# Setup left frame with checkboxes for planet selection
planets_cb_frame = tk.Frame(main, padx=5, pady=5)
planets_cb_frame.place(x=10, y=5)    
planet_vars = {}
for i, planet in enumerate(planets):
    var = tk.IntVar(value=0)  # Default to selected
    cb = tk.Checkbutton(planets_cb_frame, text=planet.name, variable=var)
    cb.pack(anchor='w')
    planet_vars[planet.name] = var 

###### TO DO ??? Add 'Select All' after all planets listed ######
# all_planets_var = tk.IntVar(value=0) 
# all_planets_checkbox = (tk.Checkbutton(planets_cb_frame, text="Select All Planets", variable=all_planets_var))
# all_planets_checkbox.pack(anchor='w')

# Setup midframe with checkboxes for planet properties 
prop_cb_frame = tk.Frame(main, padx=5, pady=5)
prop_cb_frame.place(x=110, y=5)  
mass_var = tk.IntVar(value=0)
type_var = tk.IntVar(value=0)  
orbit_au_var = tk.IntVar(value=0)
orbit_yr_var = tk.IntVar(value=0)
moons_var = tk.IntVar(value=0)
mass_checkbox = tk.Checkbutton(prop_cb_frame, text="Mass (Earth Masses)", variable=mass_var)
type_checkbox = tk.Checkbutton(prop_cb_frame, text="Type", variable=type_var)
orbit_au_checkbox = tk.Checkbutton(prop_cb_frame, text="Orbital Distance (AU)", variable=orbit_au_var)
orbit_yr_checkbox = tk.Checkbutton(prop_cb_frame, text="Orbital Period (Earth years)", variable=orbit_yr_var)
moons_checkbox = tk.Checkbutton(prop_cb_frame, text="Moons", variable=moons_var)
mass_checkbox.pack(anchor='w')
type_checkbox.pack(anchor='w')
orbit_au_checkbox.pack(anchor='w')
orbit_yr_checkbox.pack(anchor='w')
moons_checkbox.pack(anchor='w')

###### TO DO ??? Add 'Select All Characteristics' after all properties listed ######
# all_props_var = tk.IntVar(value=0)
# all_props_checkbox = tk.Checkbutton(prop_cb_frame, text="Select All Characteristics", variable=all_props_var)
# all_props_checkbox.pack(anchor='w')

# Setup text area for displaying planet information
text_area = tk.Text(main, wrap=tk.WORD, width=50, height=90)
text_area.place(x=310, y=10, relwidth=1.0, width=-325, relheight=0.96)

# Setup a button to display user-selected information
update_button = tk.Button(root, text="Update Display", command=display_planet_info)
update_button.place(x=25, y=460)

# Initialize display with default checkbox states
display_planet_info()                           

# Main Tkinter loop
root.mainloop()

# End of program