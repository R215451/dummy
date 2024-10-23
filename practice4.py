# 24 Oct 2024
#Program to print smallest and biggest possible palindrome word in a given string
name = 'Wow you own kayak'
name_list =name.split()
print(name_list)

def check_pallindrome(str):
    rev = ''
    for item in str:
        rev = item + rev  # a 
    
    if rev.lower() == str.lower():   
        return True   


res_list = []
for data in name_list:
    if check_pallindrome(data): # type: ignore
     res_list.append(data)

print(res_list)
for item in res_list:
   l = f"length of {item} is {len(item)}"
   print(l)

   print(min(res_list,key=len))
   print(max(res_list,key=len))           
    
    
# List elements rotate left side  as well as right side with 1 position 
list_of_numbers = [1,2,3,4]
# number = int(input('Enter a number , from you want to shift the elements'))
# # [2,3,4,1]
# left_side_rotation = list_of_numbers[number:]+list_of_numbers[:number]
# #[4 1 2 3]
# right_side_rotation = list_of_numbers[-number:]+list_of_numbers[:-number]
# print(left_side_rotation)
# print(right_side_rotation)


empty_list_7 = []

for i in range(1,len(list_of_numbers)):
   empty_list_7[i] = list_of_numbers[i]
print(empty_list_7)   
      



  