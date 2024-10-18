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

print("==================================================")

list_8 =  [10, 55, 4, 60, 77, 89, 90, 77, 54, 77]
list_8.sort()
#smallest element in a list 
print(list_8[0])
#Largest element in a list 
len2 = len(list_8)
result = list_8[len2-1]
print(result)

# swap 2 numbers in python 
number1 = 10
number2 = 20
temp = 0
print(number1,number2)
temp = number2
number2 = number1
number1 = temp

print(number1,number2)

print("*******************************")
number3 = 2
number4 = 3
print(number3,number4)
number3 = number3+number4
number4 = number3-number4
number3 = number3-number4

print(number3,number4)

#bubble sort concept in python
list_9 = [10, 55, 4, 60, 77, 89, 90, 77, 54, 77]
for i in range(len(list_9)):
   for j in range(len(list_9)-1):
      if list_9[j]>list_9[j+1]:
         temp = list_9[j+1]
         list_9[j+1] = list_9[j]
         list_9[j] = temp
print(list_9)

#Armstrong number calculate 
arms_number = 153
temp = arms_number
length___ = 0
while(temp!=0):
   length___ = length___+1
   temp = temp//10
print(length___)   

#Now I have to calculate armstrong number
t2 = arms_number
arm = 0
while(t2!=0):
   multi = 1
   rem = t2 % 10
   for i in range(length___):
      multi = multi * rem
   arm = arm+multi
   t2 = t2//10  

if arms_number == arm:
 print(arm,"is armstrong number:")
else:
   print(arm,"is not armstrong number")#this is armstrong number 

#**************************prime number concept in python with infinite loop 
while True:
    try:
        user_number = int(input('Enter a number as your wish: '))
        break  # Exit the loop if input is valid
    except ValueError:
        print("That's not a valid number. Please try again.")

print(user_number)
t3 = 0
for i in range(2,user_number):
   if user_number % i == 0:
      t3 = t3+1
if t3>0:
   print('Not Prime Number')
else:
   print('Prime Number')

# Fabonnaci series  of first 10 numbers in python 
num_1 = 0 
num_2 = 1
print(num_1,num_2,end=' ')
for i in range(8):
   temp = num_1+num_2
   print(temp,end=' ')
   num_1 = num_2
   num_2 = temp


