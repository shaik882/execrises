#Write a program that generate 5 random numbers in the range 10 to 50. Use a seed
#value of 6. Make a provision to change this seed value every time you execute the program
#associating it with time of execution
import random
import math
random.seed(6)
for i in range(5):
    print(random.randint(10, 50))
#a = random.seed(Random)
#print(a)