"""
Author:  Abigail Logan
Date written: 01/16/25
Assignment:   Module 1 Programming Assignment part 1
Short Desc:   This programconverts Celsius temperatures to Fahrenheit temperatures.
"""

# User enters a temperature in Celsius
celsius = float(input("Enter a temperature in Celsius: "))

# Conversion to Fahrenheit using formula F=9/5*C+32
fahrenheit = 9/5 * celsius + 32

# Display the temperature converted to Fahrenheit
print("Temperature in Fahrenheit:", fahrenheit)