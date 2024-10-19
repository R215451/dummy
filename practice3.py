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

