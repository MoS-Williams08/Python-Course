var_a = 'a'
test_word = 'January'
if var_a in test_word:
    print('There are letter a in ' + test_word)
else:
    print('There are no letter a in ' + test_word)


var_str = 'three'
bigger_str = var_str *5
print(bigger_str.count(var_str))

format_string = 'this is my {} python class{}'
print(format_string.format('2', '!'))

val = 'secret'
print(f'This is my f -string that holds the {var_str} {val}')

