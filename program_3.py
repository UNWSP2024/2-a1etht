#Programmer: Alethea Lo
#Date: 1/30/25

item1=19.99
item2=25.99
item3=5.99
item4=6.55
item5=9.99

subtotal=item1 + item2 + item3 + item4 + item5

sales_tax_rate=0.07
sales_tax=subtotal * sales_tax_rate

total=subtotal + sales_tax

#Display results
print("Subtotal:$", format(subtotal, '.2f'))
print("Sales tax (7%): $", format(sales_tax, '.2f'))
print("Total:$", format(total, '.2f'))
