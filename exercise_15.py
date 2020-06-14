#While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than
#1000. if quantity and price per item are input through the keyword, write a program to calculate the total expenses
#Author : WarLord
#Date:14-06-2020
item_quantity = int(input('Enter Value of Quantity:  '))
item_price = float(input('Enter value of the item:  '))
if item_quantity > 1000:
    dis = 10
else:
    dis = 0
total_price = item_quantity * item_price - item_quantity * item_price * dis / 100
print('Total Price = RS' + str(total_price))