#In a company an employee is paid as under:
#If his basic salary is less than Rs.11500, then HRA = 10% of basic salary
# and DA= 90% of basic salary, if his salary is either equal to or above Rs 11500 then HRA = 2%
# and DA = 98% of basic salary. If the employee's Salary is input through the keyboard write a program
#to find his gross salary
Employee_Name = input("Enter Employee Name:  ")
Basic_Salary = int(input("Enter Employee Basic salary:  "))
if Basic_Salary < 11500:
    HRA = 0.1 * Basic_Salary
    DA = 0.9 * Basic_Salary
else:
    HRA = 0.02 * Basic_Salary
    DA = 0.98 * Basic_Salary

Gross_Salary = Basic_Salary + HRA + DA
print('Salary of Employee', Employee_Name)
print(Gross_Salary)