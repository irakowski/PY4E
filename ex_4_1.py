"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
and create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except ValueError:
        print("Error, please enter numeric input")
        quit()
    
    standart_time = 40
    if hours > standart_time:
        overtime_rate = rate * 1.5 * (hours - standart_time)
        pay = (standart_time * rate) + overtime_rate
    else:
        pay = hours * rate
    return pay

hrs = input("Enter Hours:")
r = input("Enter Rate:")
print(computepay(hrs, r))