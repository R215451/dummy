print("Q1 Reverse your  name")
name  = "MAM"
reverse = ""
for data in name:
   reverse =  data + reverse 

print(reverse)   

if reverse == name:
   print("name is pallindrome")
else:
   print("Not pallindrome")   


print("LInear Search from a list in python **********")
list_7 = [10,55,4,60,77,89,90] 
number = int(input("enter a number"))

for data in list_7:
    if data == number:
      print(data,"NUmber is found ")
      break
else:
      print("Not Found")

print("Remove duplicate from a list********** Method 1 Using set collection")
list_1 = [10, 55, 4, 60, 77, 89, 90, 77, 54, 77]
set_data = set(list_1)
l1 = list(set_data) 
print(l1)

print("Method 2 , Duplicate remove using new_list creation")
list_2 = [10, 55, 4, 60, 77, 89, 90, 77, 54, 77]
new_list = []

for num in list_2:
    if num not in new_list:
        new_list.append(num)
print(new_list)
print("Ascending to a list ")
list_3 = [10, 55, 4, 60, 77, 89, 90, 77, 54, 77]
list_3.sort()
print(list_3)

print(list_3[::-1])

print("Number problem in python ")
number = 123
temp = number
reverse = 0
while(temp!=0):
 rem = temp % 10 
 reverse = reverse * 10 + rem
 temp = temp//10

print(reverse)