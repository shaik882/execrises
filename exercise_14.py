# Assume a suitable value for temperature of a city in Fahrenheit degrees. Write a program to convert this
# tempature into centigrade degrees and print both temperatures
import math
print("This program is to convert fahrenheit degrees to centigrade degress")
print("Written by Warlord")
City_Name = input("Enter the City Name >>>")
Fahrenheit_Degrees = int(input("Enter the tempature>>>"))
print("Current Tempature of", City_Name, "is", Fahrenheit_Degrees, "F")
Centigrade_Degrees = Fahrenheit_Degrees - 32
print("Current Tempature of", City_Name, "is", Centigrade_Degrees, "C")