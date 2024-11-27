# Nasheel's Repostitory: https://github.com/NasheelNadeem/Acivity4
# Sri's Repository: https://github.com/SriVignan123/Activity4
 
from polygon import Polygon

# Step 1:
def test_polygon_initialization(): # Test the initialization of the Polygon class
    p = Polygon("Triangle", [3, 3, 3]) # Create a Polygon object
    assert p.get_name() == "Triangle" # Verify the name is correctly set
    assert p.get_sides() == [3, 3, 3] # Verify the side lengths are correctly set

def test_getters_and_setters(): # Test the getter and setter methods
    p = Polygon("Square", [4, 4, 4, 4]) # Create a Polygon object
    assert p.get_name() == "Square" # Verify the initial name
    p.set_name("Rectangle") # Update the name and verify
    assert p.get_name() == "Rectangle"
    p.set_sides([4, 6, 4, 6]) # Update the sides and verify
    assert p.get_sides() == [4, 6, 4, 6]

#Step 2:
def test_polygon_equality(): # Test if two identical polygons are equal
    p1 = Polygon("Square", [4, 4, 4, 4])
    p2 = Polygon("Square", [4, 4, 4, 4])
    assert p1 == p2 # Verify they are equal

def test_polygon_inequality(): # Test if two different polygons are not equal
    p1 = Polygon("Square", [4, 4, 4, 4])
    p2 = Polygon("Rectangle", [4, 6, 4, 6])
    assert p1 != p2 # Verify they are not equal

# Step 3:
def test_polygon_str(): # Verify the string representation is formatted correctly
    p = Polygon("Triangle", [3, 3, 3])
    assert str(p) == "Triangle with sides: [3, 3, 3]"

# Step 4:
def test_calculate_circumference(): # Verify that the circumference is calculated correctly
    p = Polygon("Triangle", [3, 3, 3])
    assert p.calculate_circumference() == 9

# Use "pytest test_polygon.py" in the terminal to test the code