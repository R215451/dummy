import string

import math,string

from num2words import num2words

name = "abc 123"
new_list = name.split()
print(new_list)

reverse_list = new_list[::-1]
print(reverse_list)

print(' '. join(reverse_list))
user_number = 0
while True:
    try:

        user_number = int(input('Enter a number as your wish: '))
        break  # Exit the loop if input is valid
    except ValueError:
        print("That's not a valid number. Please try again.")
       
converted_number = num2words(user_number)
print(converted_number)


# Anagrams of two strings 
str1 = input('Enter a string 1 ')
str2 = input('Enter a string 2 ')

str1 = str1.replace(' ','').lower()
str2 = str2.replace(' ','').lower()

if sorted(str1) == sorted(str2):
    print('Anagrams')
else:
    print('Not Anagrams')