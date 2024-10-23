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
    
    




  