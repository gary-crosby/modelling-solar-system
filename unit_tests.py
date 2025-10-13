"""
Unit tests for model_solar_system.py

This module contains unit tests for classes: Planet, MoonPerm.

Created by Gary Crosby for SHU MSc Computer Science module 'Fundamentals of Computing'
"""

import unittest
import sys
import os
import math

# Add current directory to the Python path to import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from model_solar_system import Planet, Reference

class TestPlanet(unittest.TestCase):
    """Test cases for the Planet class."""
    
    def setUp(self):
        
        # Create test data for a planet with 0 moons and 0 provisional moons
        self.venus = Planet(
             "Venus",
              4.87e+24,
              "Terrestrial",
              108200000,
              0.62
              )

        # Create test data for a planet with 1 moon and 0 provisional moons
        self.earth = Planet(
             "Earth",
              5.97e+24,
              "Terrestrial",
              149600000,
              1.00,
              ["Moon"]
              )
        
        # Create test data for >1 moons and >1 provisional mmons
        # Note: Jupiter has many perm moons but to save time we'll use only 4
        self.jupiter = Planet(
              "Jupiter",
              1.90e+27,
              "Gas Giant",
              778500000,
              11.86,
              ["Io", "Europa", "Ganymede", "Callisto"],
              54
              )
        # 

        # Add setup for DataSources here

    def test_planet_properties(self):
        """Test all Planet properties except mass_earth."""

        # Venus
        assert self.venus.name == "Venus", "Planet name incorrect"
        assert self.venus.mass_kg == 4.87e+24, "Planet mass incorrect"
        assert self.venus.type == "Terrestrial", "Planet type incorrect"
        assert self.venus.orbit_au == 0.72, "Planet distance from Sun incorrect"    
        assert self.venus.orbit_yr == 0.62, "Planet orbital period incorrect"
        assert self.venus.moons_perm == [], "Planet permanent moons name(s) incorrect"  
        assert self.venus.moons_prov_n == 0, "Planet provisional moons count incorrect"
        
        # Earth
        assert self.earth.name == "Earth", "Planet name incorrect"
        assert self.earth.mass_kg == 5.97e+24, "Planet mass incorrect"
        assert self.earth.type == "Terrestrial", "Planet type incorrect"
        assert self.earth.orbit_au == 1.00, "Planet distance from Sun incorrect"    
        assert self.earth.orbit_yr == 1.00, "Planet orbital period incorrect"
        assert self.earth.moons_perm == ["Moon"], "Planet permanent moons name(s) incorrect"  
        assert self.earth.moons_prov_n == 0, "Planet provisional moons count incorrect"

        # Jupiter
        assert self.jupiter.name == "Jupiter", "Planet name incorrect"
        assert self.jupiter.mass_kg == 1.9e+27, "Planet mass incorrect"
        assert self.jupiter.type == "Gas Giant", "Planet type incorrect"
        assert self.jupiter.orbit_au == 5.2, "Planet distance from Sun incorrect"    
        assert self.jupiter.orbit_yr == 11.86, "Planet orbital period incorrect"
        assert self.jupiter.moons_perm == ["Io", "Europa", "Ganymede", "Callisto"], "Planet permanent moons name(s) incorrect"  
        assert self.jupiter.moons_prov_n == 54, "Planet provisional moons count incorrect"

    # Add test(s) for References here

if __name__ == "__main__":
  unittest.main() # run all tests
