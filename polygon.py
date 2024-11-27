class Polygon:
    # Step 1:
    def __init__(self, name, sides): # Initialize the name and sides of the polygon
        self.name = name
        self.sides = sides

    # Getters
    def get_name(self):
        return self.name

    def get_sides(self):
        return self.sides

    # Setters
    def set_name(self, name):
        self.name = name

    def set_sides(self, sides):
        self.sides = sides

    # Step 2:
    def __eq__(self, other):
        return self.name == other.name and self.sides == other.sides  # Returns True if both polygons names and side lengths are the same

    def __ne__(self, other):
        return not self.__eq__(other) # Returns False if both polygons names and side lengths are the same

    
    # Step 3:
    def __str__(self):
        return f"{self.name} with sides: {self.sides}" # Returns a string
    
    # Step 4:
    def calculate_circumference(self):
        return sum(self.sides) # Return the sum of all the side lengths

# Step 5:
def main():
    # Create instances of different polygons
    triangle = Polygon("Triangle", [3, 3, 3])
    square = Polygon("Square", [4, 4, 4, 4])
    hexagon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])

    # Iterate through the polygons and print their values
    for polygon in [triangle, square, hexagon]:
        print(polygon)
        print(f"Circumference= {polygon.calculate_circumference()}")

if __name__ == "__main__":
    main()