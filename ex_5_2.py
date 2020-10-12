""" Exercise 2: Write another program that prompts for a list of numbers  
and at the end prints out both the maximum and minimum of the numbers"""

numbers = list()
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try: 
        num = int(num)
        numbers.append(num)
    except:
        print('Invalid input')

if numbers:
    max_value = None
    min_value = None
    for num in numbers:
        if min_value is None or min_value > num:
            min_value = num
        if max_value is None or max_value < num:
            max_value = num
    print("Min value:",min_value, "\nMax value:", max_value)

