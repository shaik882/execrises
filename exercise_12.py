# Assume a suitable value of Ramesh's basic salary. His dearness allowance is 40% of basic salary, and house
# rent allowance is 20% of basic salary. Write a program to calculate his gross salary.
basic_Salary = int('90000')
dearness_allowance = int(90000 * 0.4)
rent_allowance = int(90000 * 0.2)
Monthly_gross_salary = basic_Salary+dearness_allowance+rent_allowance
#Yearly_gross_salary = int('Monthly_gross_salary') * 12
print(Monthly_gross_salary * 12)
# gross_salary = Monthly_gross_salary * 12
# print(gross_salary)