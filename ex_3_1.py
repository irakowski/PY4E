"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate
for hours worked above 40 hours
"""
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

standart_time = 40
if hours > standart_time:
    overtime_rate = rate * 1.5 * (hours - standart_time)
    pay = (standart_time * rate) + overtime_rate
else:
    pay = hours * rate

print("Pay: ", pay)