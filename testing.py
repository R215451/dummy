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

# input_string = input('Enter your name ')
# perms = itertools.permutations(input_string)
# result =  [''.join(p) for p in set(perms)]
# print(result)

#Left side rotation 
# empty_list = []
# list_of_numbers = [1,2,3,4] # [2 3 4 1]
# for i in range(1,len(list_of_numbers)):
#     empty_list.append(list_of_numbers[i])


# empty_list.append(list_of_numbers[0])


#Right side rotation
#[4 1 2 3]

# empty_list.append(list_of_numbers[-1])
# for i in range(0,len(list_of_numbers)-1):
#     empty_list.append(list_of_numbers[i])
# print(empty_list)    


print('Assignment for 25 OCT 2024 STARTING FROM HERE')
print('Question 1 Find one string is rotation of another string')
name_1 = 'abcdef'
name_2 = 'defabc'

name_1 = name_1+name_1
if name_2 in name_1:
    print('Rotation')
else:
    print('No Rotation') 

print('Question 2 Divide string in n equal parts')

name_3 = 'abcde'
divide = 2 
number_parts = len(name_3) // divide    
rem = len(name_3) % divide    


list_new = []
start=0
for i in range(divide):
  end = start + number_parts +  (1 if rem > 0 else 0)
  list_new.append(name_3[start:end])
  start = end
  rem-=1
print(list_new)  


print('Question 3 Find subset of a string')
name_4 = 'abc'
subset = ['']
for char in name_4:
   subset_list = []
   for item in subset:
      subset_list.append(item+char)
   subset = subset + subset_list 
print(subset)     

print('Question 4 Find permutations of a string')
#creating a function 
def calc_perm(name):
   if len(name) == 0:
      return []
   if len(name) ==1:
      return [name]
    
   new_list_for_permutations = []
   for i in range(len(name)):
      current_char = name[i]
      remaining_string_chars = name[:i]+name[i+1:]
      for item in calc_perm(remaining_string_chars):
         new_list_for_permutations.append(item+current_char)
   return new_list_for_permutations

# Now calls to function above
print(calc_perm('abc'))

print('Question 5 Max and Min sequence of character')

name_of_college = 'Asansol Engineering College'.lower()
item_smaple_dict = {}
for item in name_of_college:
   if item in item_smaple_dict:
    item_smaple_dict[item] += 1 
   else:
      item_smaple_dict[item] = 1
print(item_smaple_dict)  
print(item_smaple_dict[max(item_smaple_dict,key=item_smaple_dict.get)])  
print(item_smaple_dict[min(item_smaple_dict,key=item_smaple_dict.get)])    


print('Question 6 Left side rotation of a list elements with 1 position')
list_left_side_rotation = [1,2,3,4] # [2 3 4 1]
print(list_left_side_rotation[1:] + list_left_side_rotation[:1])      
    
print('Question 7 Right side rotation of a list elements with 1 position')
list_right_side_rotation = [1,2,3,4] # output [4,1,2,3]
print(list_right_side_rotation[-1:]+list_right_side_rotation[:-1])



 