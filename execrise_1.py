#Execrise 1 - Price of house is $1M, if buyer has good credit score,
# they need to put down 10% otherwise they need to putdown 20%
#Author "Fareeduddin Shaik
#import math
price = 10
print(price)
Gross_Salary = int(input('What is your Gross Salary: '))
Credit_Score = int(input('What is your Credit_Score: '))
house_price = int(input('Enter the house price: '))

if Credit_Score > 550 and Gross_Salary > 90000:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print ({down_payment})