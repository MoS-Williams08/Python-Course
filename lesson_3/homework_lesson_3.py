# Enter two numbers. 
first_number = 5
second_number = 9

#If the first one is greater than the second, save first number in result_1,

result_1 = ''
if first_number > second_number: 
    result_1 = first_number

# otherwise save the second number to the result_1 variable.

else: result_1 = second_number
print(result_1)

#####################################


# Enter a random number in number_1 variable. 
import random
number_1 = random.randint(1,100)
result_2 = []
#If this number is 20 or higher save “Too high” text to result_2, otherwise save “Thank you”

if number_1 > 20:
    result_2 = 'Too high'
else: 
    result_2 = 'Thank you'
    
print(result_2, number_1)




#####################################



# Enter your first name and last name in first_name and last_name variables.
first_name = 'david'
last_name = 'colonia'

# If the length of your first name is under five characters, join them together (without a space) and save it to result_3 variable in upper case.

if len(first_name) <= 5:
    result_3 = (first_name + ' ' + last_name).capitalize()
# If the length of the first name is five or more characters, save their first name in lower case in result_3 variable.

else: 
    result_3 = None
print(result_3)

#####################################


# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
number_2 = input('enter a number between 10 and 20:')
number_2 = int(number_2)
# If they enter a number within this range, save a message “Thank you” to result_4,
if number_2 >= 10 and number_2 <= 20:
    result_4 = 'thank you'
# otherwise a message “Incorrect answer” to result_4.
else:
    result_4 = 'incorrect result'
print(result_4)

#####################################




# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,

age = random.randint(10,25)
if age > 18:
    result_5 = 'you can vote'
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,

elif age > 17: 
    result_5 = 'you can drive'
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
elif age > 16:
    result_5 = 'you can buy a lottery ticket'
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

else:
    result_5 = 'you can go trick or treating'
print(f'you are {age} years old,')
print(result_5)
#####################################




# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = input('Enter a number between 1 and 12:')
month = int(month)
if month == 1:
    result_month = 'January'
elif month == 2:
    result_month = 'Feb'
elif month == 3:
    result_month = 'Feb'
elif month == 4:
    result_month = 'Apr'
elif month == 5:
    result_month = 'may'
elif month == 6:
    result_month = 'jun'
elif month == 7:
    result_month = 'jul'
elif month == 8:
    result_month = 'aug'
elif month == 9:
    result_month = 'sep'
elif month == 10:
    result_month = 'oct'
elif month == 11:
    result_month = 'nov'
elif month == 12:
    result_month = 'dec'
print(result_month)



##########################################################################3.2#############################################################

# Else save the text "Wrong value" to result_1

# Enter a number between 1 and 20, save this value to number variable.

number = input('enter the number')
number = int(number)
# If number is greater than 0 and less than or equal to 7, save the number * 10 to result_1.

if number > 0 and number <= 7:
    result_1 = number * 10
# If number is  greater than 7 and less than or equal to 15, save the result of floor division of the number divided by  3 to result_1 variable

elif number > 7 and number <= 15:
    result_1 = floor(number / 3)
# If number is  greater than 15 and less than or equal to 20, save the number raised to the power 3 to result_1

elif number > 15 and number <= 20: 
    result_1 = number ** 3
    
# Else save the text "Wrong value" to result_1

else:
    result_1 = "wrong value"
print(result_1)

##########################################################################



# Enter two numbers between 1 and 10, save this values to number_1 variable and number_2 variables.

number_1 = int(input('Enter first value:'))
number_2 = int(input('Enter second value:'))

# If number_1 and number_2 are greater than 0 and less than or equal to 5 save in the product of their multiplication  to result_2

if number_1 > 0 and number_2 > 0 and number_1 <= 5 and number_2 <= 5:
    result_2 = number_1 * number_2
    
# If one of the variables (number_1 or number_2) is greater than 5 and less than or equal to 10, but the other isn't, then save the sum of the two numbers to result_2

elif (number_1 > 5 and number_1 <= 10 and not (number_2 > 5 and number_2 <= 10)) or (number_2 > 5 and number_2 <= 10 and not (number_1 > 5 and number_1 <= 10)):
    result_2 = number_1 + number_2
    
# If both numbers are greater than 5 and less than or equal to 10, multiply their sum by 3 and save it to result_2

elif number_1 > 5 and number_1 <= 10 or number_2 > 5 and number_2 <= 10:
    result_2 = (number_1 + number_2) * 3
    
# Else save the text "Wrong values, try again" to result_2

else: 
    "wrong values, try again"
print(result_2)
##########################################################################




first_name = 'david'
last_name = 'colonia'

# If first_name or last_name are shorter than 6 characters, save a full name (with a space between) to result_3

if len(first_name) < 6 or len(last_name) < 6:
    result_3 = first_name + ' ' + last_name
    
# Enter your first name and save it to first_name variable, then Enter last name and save it to last_name

    
else:
    result_3 = first_name * len(last_name)
print(result_3)


##########################################################################

# Enter a random number. Save this value to random_number variable

import random
random_number = random.randint(1,1000)

# If this number is less 10 or greater than 99, save the text "Please, put in a number between 10 and 99" to result_4

if random_number < 10:
    if random_number > 99:
        result_4 = 'Please put in a number between 10 and 99'
# If a number doesn't meet the first condition, find the remainder of random_value divided by 2.
        
else: 
    remainder = random_number % 2
    if remainder == 0:
        result_4 = 'Even number'
        
# If it is 0, save the text "Even number" to result_4 , else save the message "Odd number"

        
    else:
        result_4 = 'odd number'
print(result_4, random_number)