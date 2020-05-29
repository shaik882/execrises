#Write a program to find the largest number is series
series = [ 50, 20, 55, 120, 66, 80, 84, 33, 90 ]
max = series[0]
for large in series:
    if large > max:
        max = large
print(max)