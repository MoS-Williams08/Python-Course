# FUNCTIONS
import random

# Difference
# Write a function, which will calculate the difference of these two numbers
import random

def difference(num_1, num_2):
    return num_1 - num_2

# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    return num_1 / num_2


# Function gets random number. If this number is more than ten, return the difference between 100 and this
# number, otherwise return this number multiplied by 10

def function_1(number):
    if number > 10:
        return 100 - number
    else:
        return number * 10
var = random.randint(1,100)
print(var)
print("The number is " + str(function_1(var)))

''' another way to skip else 
def function_1(number):
    if number > 10:
        return 100 - number
    return number * 10
'''
# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and
# return Formula (32°F − 32) × 5/9 = 0°C

def temerature_convertor(fahrenheit_degree):
    celsius = (fahrenheit_degree - 32) * 5/9
    return  celsius
print("Temp convertor: " + str(temerature_convertor(32)))


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters
# travelled. Write a function that takes the distance travelled (in kilometers) as its only parameter and
# returns the total fare as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    meters = distance * 1000
    cost = 4.00 + meters/140 * 0.25
    return cost.__round__(2)
print("taxi fare: " + str(taxi_fare((10))))

# examples of usage:
# taxi_fare(10) #21.86