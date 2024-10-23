# # import string

# # import math,string

# # from num2words import num2words

# # name = "abc 123"
# # new_list = name.split()
# # print(new_list)

# # reverse_list = new_list[::-1]
# # print(reverse_list)

# # print(' '. join(reverse_list))
# # user_number = 0
# # while True:
# #     try:

# #         user_number = int(input('Enter a number as your wish: '))
# #         break  # Exit the loop if input is valid
# #     except ValueError:
# #         print("That's not a valid number. Please try again.")
       
# # converted_number = num2words(user_number)
# # print(converted_number)


# # # Anagrams of two strings 
# # str1 = input('Enter a string 1 ')
# # str2 = input('Enter a string 2 ')

# # str1 = str1.replace(' ','').lower()
# # str2 = str2.replace(' ','').lower()

# # if sorted(str1) == sorted(str2):
# #     print('Anagrams')
# # else:
# #     print('Not Anagrams')

# # divide_string = input('Enter your name ')
# # number_of_division = int(input('Entre a number in which do you want to divide your name '))
# # l1 = len(divide_string)
# # part_length = l1 // number_of_division
# # remender = l1 % number_of_division

# # parts = []
# # start = 0
# # for i in range(number_of_division):
# #      end = start + part_length + (1 if remender > 0 else 0)
# #      parts.append(divide_string[start:end]) 
# #      start = end
# #      remender = remender - 1

# # print(parts)


# string = input('Enter your name ')
# subsets = [""]
# for char in string:
#   new_subsets = []

#   for subset in subsets:
#         new_subset = subset+char
#         new_subsets.append(new_subset)
#   subsets = subsets+new_subsets

# print(subsets)

import itertools

# def string_permutations(s):
#     # Generate all permutations
#     perms = itertools.permutations(s)
#     # Convert tuples to strings and return a list of unique permutations
#     print(perms)
#     return [''.join(p) for p in set(perms)]

# # Example usage
# input_string = "abc"
# result = string_permutations(input_string)
# print(result)

input_string = input('Enter your name ')
perms = itertools.permutations(input_string)
result =  [''.join(p) for p in set(perms)]
print(result)
