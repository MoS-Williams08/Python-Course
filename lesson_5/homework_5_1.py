# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    return num_1-num_2
difference(4,5)


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    return num_1 / num_2
division(2,4)

# Function gets random number. If this number is more than ten, return the difference between 100 and this number,

def function_1(number):
    if number > 10:
        return 100 - number 
    
# otherwise return this number multiplied by 10

    else: 
        return number * 10 
function_1(10)

# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temerature_convertor(fahrenheit_degree):
    celcius = (fahrenheit_degree - 32) * 5/9
    return celcius
temerature_convertor(32)


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

import math
def taxi_fare(distance):
    meters = distance * 1000
    total_fare = 4.00 + (.25*(meters/140))
    return total_fare.__round__(2)
taxi_fare(10)
# examples of usage:
# taxi_fare(10) #21.86



