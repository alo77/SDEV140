"""
Author:  Abigail Logan
Date written: 01/20/25
Assignment:   Module 1 Programming Assignment part 1
Short Desc:   This program calculates the surface area of a cube by asking for the edge length, then using the formula 6 × (edge length)**2 to display the result.
"""

# Print the docstring (introductory message)
print("Docstring: This program calculates the surface area of a cube by asking for the edge length, then using the formula 6 × (edge length)**2 to display the result.")

# User input edge length
user_input = input("Enter the cube's edge length (integer): ")
edge_length = int(user_input)

# Calculate surface area
surface_area = 6 * (edge_length ** 2)

# Print result
print("The surface area of the cube is:", surface_area)