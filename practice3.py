# # remove all white spaces from given string 
# name = "abc cde cdfscgcbhs "
# print(name.replace(' ',''))

# # remove all  from lower to upper or viceversa  
# name_1 = "abc cde cdfscgcbhs ".upper()
# print(name_1)# Converted in upper case

# #replace the spaces of a string with a specific character
# name_2 = input('Enter your name ')
# new_str = name_2.replace(' ','@')
# print(new_str)
# #find the duplicate characters in a string
# name_3 = input('Enter your name ')
# name_3_3 = ''
# for item_char in name_3:
#     if item_char not in name_3_3:
#         name_3_3 = name_3_3+item_char
    
# print(name_3)
# print(name_3_3)    

# #find the duplicate words in a string
# name_4  = "ABC BCD ABC"
# empty_list = []
# list_name = name_4.split()
# for i in list_name:
#     if i not in empty_list:
#         empty_list.append(i)
# print(' '.join(empty_list))    

# #find frequency of characters in python 
# name_5 = "abcvhvcsahvcskhkbcsk"
# frequency = {}
# for i in name_5:
#     if i in frequency:
#         frequency[i] = frequency[i]+1
#     else:
#         frequency[i] = 1

# print(frequency)

# # Swap of two strings in python without using third variable 
# name_6 = input('Enter your name ')
# name_7 = input('Enter your name ')
# print(name_6,name_7)
# name_6, name_7 = name_7,name_6
# print(name_6,name_7)

# #Find the sum of natural numbers  1 2 3 4 5 
# sum_natural_numbers =0
# for i in range(1,101):
#     sum_natural_numbers = sum_natural_numbers + i
# print(sum_natural_numbers)

# #Find the sum of list numbers 
# list_1 = [10,20,4,77,7,87,45]
# sum_of_list_numbers  = 0
# for i in list_1:
#    sum_of_list_numbers = sum_of_list_numbers + i
# print(sum_of_list_numbers)

# divide string in n equal parts 
divide_string = "abcdefghijk"
number_of_division = 3
l1 = len(divide_string)
part_length = l1 // number_of_division
remender = l1 % number_of_division

parts = []
start = 0
for i in range(number_of_division):
    end = start + part_length + (1 if remender > 0 else 0)
    parts.append(divide_string[start:end])
    start = end
    remender = remender -1 

print(parts) 


# Define two sets
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

# Check if set_a is a subset of set_b
is_subset = set_a.issubset(set_b)

print(is_subset)

string = "abc"
subsets = [""]
for char in string:
  new_subsets = []
  for subset in subsets:
     new_subset = subset+char
     new_subsets.append(new_subset)

  subsets  = subsets+new_subsets 

print(subsets) 
 

