"""Exercise 5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature."""

temp_cels = float(input("Enter temperature in Celsius: "))
temp_fah = (temp_cels * 1.8) + 32
print(f"{temp_cels}C is approx. {temp_fah}F")