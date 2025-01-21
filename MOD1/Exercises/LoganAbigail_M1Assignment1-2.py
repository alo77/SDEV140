"""
Author:  Abigail Logan
Date written: 01/20/25
Assignment:   Module 1 Programming Assignment Part 2
Short Desc:   This program asks the user for the meal's cost, computes an 18% tip and 7% sales tax, and then displays these amounts along with the total.
"""

# User inputs the meal cost
meal_cost = float(input("Enter the cost of your meal: "))

# Calculate tip (18%)
tip = meal_cost * 0.18

# Calculate sales tax (7%)
tax = meal_cost * 0.07

# Calculate total amount
total_cost = meal_cost + tip + tax

# Print tip, tax, and total
print("Tip:", tip)
print("Tax:", tax)
print("Total cost:", total_cost)