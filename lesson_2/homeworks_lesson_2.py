# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'string'
result_string_2 = "string"
result_string_3 = """string 
                    string"""
print(result_string_1)
print(result_string_2)
print(result_string_3)
##################################################################


# Enter your first and  last name. 
first_name = "david"
last_name = "colonia"
# Join them together with a space in between.
#Save a result in a variable result_full_name and save the length of the whole name in result_full_name_length variable.
result_full_name = first_name + " " + last_name
result_full_name_length = len(result_full_name)
print(result_full_name)
print(result_full_name_length)

##################################################################


# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

result_ca_capital = 'sacramento'
print(result_ca_capital.title())

##################################################################


# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable

result_planet = 'earth'
print(result_planet.upper())



##############################################################2.2######################################################################

# Change result_string_1 that 'very simple language' will be displayed on a new line
result_string_1 = 'Python is the \n very simple language'
print(result_string_1)

##################################################################

# Change result_string_2 to print out the phrase: 'What does the word 'integer' mean'
result_string_2 = 'What does the word \'integer\' mean'
print(result_string_2)


##################################################################
# Assign number variable to value "5" (as a string). 
number = '5'
# rise the number to the power 3 & Save the expression to result_value variable
result_value = int(number) ** 3
print(result_value)

##################################################################

# Enter a random number, then save the value to n variable.
import random
n = random.randint(0,10)
# repeat the variable "word" n times and save the value to result_string_3
word = 'super'
result_string_3 = word*n
print(result_string_3)


##############################################################2.3######################################################################




# Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

# type your code here
temperature_fahrenheit = '75'
result_temperature = (int(temperature_fahrenheit) - 32) * 5/9 
print(result_temperature)















