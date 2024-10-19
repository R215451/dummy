# remove all white spaces from given string 
name = "abc cde cdfscgcbhs "
print(name.replace(' ',''))

# remove all  from lower to upper or viceversa  
name_1 = "abc cde cdfscgcbhs ".upper()
print(name_1)# Converted in upper case

#replace the spaces of a string with a specific character
name_2 = input('Enter your name ')
new_str = name_2.replace(' ','@')
print(new_str)
#find the duplicate characters in a string
name_3 = input('Enter your name ')
name_3_3 = ''
for item_char in name_3:
    if item_char not in name_3_3:
        name_3_3 = name_3_3+item_char
    
print(name_3)
print(name_3_3)    

#find the duplicate words in a string
name_4  = "ABC BCD ABC"
empty_list = []
list_name = name_4.split()
for i in list_name:
    if i not in empty_list:
        empty_list.append(i)
print(' '.join(empty_list))    

#find frequency of characters in python 
name_5 = "abcvhvcsahvcskhkbcsk"
frequency = {}
for i in name_5:
    if i in frequency:
        frequency[i] = frequency[i]+1
    else:
        frequency[i] = 1

print(frequency)

# Swap of two strings in python without using third variable 
name_6 = input('Enter your name ')
name_7 = input('Enter your name ')
print(name_6,name_7)
name_6, name_7 = name_7,name_6
print(name_6,name_7)