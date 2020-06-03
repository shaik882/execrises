# Assume a suitable value for distance between two sites (in KMs). Write a Program to convert and print this distance
# into meters, Feet, Inches and Centimeters

import math
print('This Program is to convert KM to meters, feets and centimeters')
print('written by warlord')
City1 = input("What is the name of the start city>>> ")
City2 = input("What is the name of the destination city>>> ")
x = int(input("Enter the distance in KM>>>"))
print("The distance between", City1, "and", City2, "is", x, "KM")
y = x * 1000
print("The distance between", City1, "and", City2, "is", y, "Meters")
z = x * 3280
print("The distance between", City1, "and", City2, "is", z, "Feet")
a = x * 39370
print("The distance between", City1, "and", City2, "is", a, "Inches")
b = x * 100000
print("The distance between", City1, "and", City2, "is", b, "Inches")
