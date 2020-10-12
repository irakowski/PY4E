"""
Exercise 2: Rewrite your pay program using try and except 
so that your program handles non-numeric input gracefully by printing a message 
and exiting the program. The following shows two executions of the program:
"""
hours = input("Enter Hours: ")
try:
    hours = float(hours)
    rate = input("Enter Rate: ")
    try: 
        rate = float(rate)
    except ValueError:
        print("Error, please enter numeric input")
except ValueError:
    print("Error, please enter numeric input")
    #quit() for stopping the program

if isinstance(hours, (float)) and isinstance(rate, (float)):
    standart_time = 40
    if hours > standart_time:
        overtime_rate = rate * 1.5 * (hours - standart_time)
        pay = (standart_time * rate) + overtime_rate
    else:
        pay = hours * rate
    print("Pay: ", pay)

