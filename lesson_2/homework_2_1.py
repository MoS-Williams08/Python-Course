# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'string'\
                  '1'
result_string_2 = "string2"
result_string_3 = '''multi
                     line
                     string'''

unicode_example = '\u0032'
print(result_string_1,result_string_2,result_string_3)
print(unicode_example)



string_var ='Careerist'
string_var1 = 'is kewl'
numeric_var = 100
percent_sign = '%'
full_string = string_var + ' ' + string_var1 + str(numeric_var) + percent_sign
print(full_string)


# Enter your first and  last name. Join them together with a space in
# between. Save a result in a variable result_full_name and
# save the length of the whole name in result_full_name_length variable.


first_name = 'Leena'
last_name = 'B'
#result_full_name = None
result_full_name = first_name + ' ' + last_name
#result_full_name_length = None
result_full_name_length = len(result_full_name)
print(result_full_name, result_full_name_length)

# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

result_ca_capital = 'sacramento'
print(result_ca_capital.capitalize())

# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable

result_planet = 'Earth'
print(result_planet.title())