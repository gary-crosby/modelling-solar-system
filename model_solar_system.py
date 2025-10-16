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
* This script reads all data from solar_system_data.json which must be in the same folder.
* Units chosen for mass (Earth mass), orbital distance (AU), and orbital period (Earth years) 
  are commonly used in astronomy. See https://en.wikipedia.org/wiki/Astronomical_system_of_units 
  The number of decimal places have been chosen to provide useful precision without excessive detail.
* The number of permanently named moons and provisional moons varies with the data source and date.
  The data used were accurate as of mid-2025.

Created by Gary Crosby for as the Final Assessment project in SHU's online
MSc Computer Science module 'Fundamentals of Computing'.

October 2025
"""

########## Setup ##########
 
### Standard library imports ###

import json
from pathlib import Path
import tkinter as tk

### Classes ###

class Planet:
    def __init__(self, name, mass_kg, type, orbit_km, orbit_yr, moons_perm=None, moons_prov=0, mass_earth=0, orbit_au=0):
        """ Initialize a Planet instance.

            Property mass_earth is mass relative to Earth and is set AFTER Planet is instantiated.
            Property orbit_au is distance from sun in Astronomical Units (AU) and is calculated here where 1 AU == 149,597,870.7 km
            A class could have been created for permanent moons but seeing as the only property of moons
            stored is their name(s), then a list is a simpler and more appropriate data structure.
        """
        self.name = name
        self.mass_kg = mass_kg
        self.type = type
        self.orbit_au = round((float(orbit_km/149597870.7)), 2) 
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

### Functions ###

def getJSON():
    """ Load the JSON file located in the same folder as this script and return the dict.
        
        Returns None on failure and prints an error message with details.

        I used the following resources when working with JSON:
            https://docs.python.org/3/library/json.html
            https://docs.python.org/3/library/pathlib.html#module-pathlib
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

def display_planet_info(info_str=""):
    """ Display information based on selected planet(s) and characteristic(s) """
    text_area.delete(1.0, tk.END)  # Clear existing text
    info = ""
    # Loop through planets and characteristics to build string to display
    for planet in planets:
        if not planet_vars[planet.name].get():
            continue  # Skip this planet if not selected
        info = f"Planet: {planet.name}\n"
        if mass_var.get():
            info += f"Mass: {planet.mass_earth} Earth masses\n"
        if type_var.get():
            info += f"Type: {planet.type}\n"  
        if orbit_au_var.get():
            info += f"Orbital distance: {planet.orbit_au} AU\n"
        if orbit_yr_var.get():
            info += f"Orbital period: {planet.orbit_yr} Earth years\n"
        if moons_var.get():
            if len(planet.moons_perm) > 0:
                info += f"Permanently named moons: {len(planet.moons_perm)}, named {', '.join(planet.moons_perm)}\n"
            else:
                info += "Permanently named moons: None\n"
            if planet.moons_prov_n > 0:
                info += f"Provisional moons: {planet.moons_prov_n}\n"
            else:
                info += "Provisional moons: None\n"
        text_area.insert(tk.END, info + "\n")
    # Add data sources at the end only if there is planet info to display
    if info !="":
        info = "Data Sources:\n"
        for ref in references:
            info += f"{ref.name} ({ref.url})\n"
        text_area.insert(tk.END, info)
    # Disable button until user changes selection again
    update_button.config(state=tk.DISABLED)  

def validate_user_input():
    """ User input is validated by enabling/disabling 'Update Display' button.
    
        The user uses checkboxes to select any combination of planets and characteristics
        including none at all. The button is only enabled when at least one planet AND
        at least one characteristic are selected.
    """
    if any(var.get() for var in planet_vars.values()) and any([mass_var.get(), type_var.get(), orbit_au_var.get(), orbit_yr_var.get(), moons_var.get()]):
        update_button.config(state=tk.NORMAL)
    else:
        update_button.config(state=tk.DISABLED)

########## Main Program ########## 

### Load data from JSON, and create Planet and Reference instances ###

# Load JSON data into a dictionary
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
# because later we will display them in that order.
planets.sort(key=lambda p: p.orbit_au)   

# Create a list of references (i.e., data sources)
references = []
for ref_data in planets_dict.get('references', []):
    reference = create_reference(ref_data)
    references.append(reference)

### Create GUI using tkinter ###
#
#   I referred to the following resources when creating and working with the GUI:
#       https://www.pythontutorial.net/tkinter/
#       https://docs.python.org/3/library/tkinter.html

# Setup GUI window
root = tk.Tk()
root.title("Solar System Planets Explorer")
root.geometry("750x500") # Should fit on monitors as small as 800x600    
root.resizable(False, False)

 # Setup main frame
main = tk.Frame(root, padx=10, pady=10)
main.pack(expand=True, fill='both')

# Setup left frame with checkboxes for planet selection.
# Planet checkboxes are created dynamically so that if the number
# of planets changes then the GUI will adapt automagically.
planets_cb_frame = tk.Frame(main, padx=5, pady=5)
planets_cb_frame.place(x=10, y=5)    
planets_label = tk.Label(planets_cb_frame, text="Select planet(s):", font=("Arial", 9, "bold") )
planets_label.pack(anchor='w')
planet_vars = {}
for i, planet in enumerate(planets):
    var = tk.IntVar(value=0)  # Default to selected
    cb = tk.Checkbutton(planets_cb_frame, text=planet.name, variable=var, command=validate_user_input)
    cb.pack(anchor='w')
    planet_vars[planet.name] = var 

# Setup mid frame with checkboxes for planet properties. 
prop_cb_frame = tk.Frame(main, padx=5, pady=5)
prop_cb_frame.place(x=130, y=5)  
prop_label = tk.Label(prop_cb_frame, text="Select characteristic(s):", font=("Arial", 9, "bold"))
prop_label.pack(anchor='w')
mass_var = tk.IntVar(value=0)
type_var = tk.IntVar(value=0)  
orbit_au_var = tk.IntVar(value=0)
orbit_yr_var = tk.IntVar(value=0)
moons_var = tk.IntVar(value=0)
mass_checkbox = tk.Checkbutton(prop_cb_frame, text="Mass", variable=mass_var, command=validate_user_input)
type_checkbox = tk.Checkbutton(prop_cb_frame, text="Type", variable=type_var, command=validate_user_input)
orbit_au_checkbox = tk.Checkbutton(prop_cb_frame, text="Orbital distance", variable=orbit_au_var, command=validate_user_input)
orbit_yr_checkbox = tk.Checkbutton(prop_cb_frame, text="Orbital period", variable=orbit_yr_var, command=validate_user_input)
moons_checkbox = tk.Checkbutton(prop_cb_frame, text="Moons", variable=moons_var, command=validate_user_input)
mass_checkbox.pack(anchor='w')
type_checkbox.pack(anchor='w')
orbit_au_checkbox.pack(anchor='w')
orbit_yr_checkbox.pack(anchor='w')
moons_checkbox.pack(anchor='w')

# Setup text area for displaying user-selected planet information.
text_area = tk.Text(main, wrap=tk.WORD, width=50, height=90)
text_area.place(x=330, y=10, relwidth=1.0, width=-345, relheight=0.96)
# Display initial instructions in text area
text_str = "Select planet(s) and characteristic(s), and then select 'Update Display'"
text_area.insert(tk.END, text_str)  

# Setup 'Update Display' button to update user-selected information.
# Button is disabled by default.
update_button = tk.Button(root, text="Update Display", command=display_planet_info, state=tk.DISABLED)
update_button.place(x=227, y=456)
                         
# Main tkinter loop
root.mainloop()

########## End of program ##########