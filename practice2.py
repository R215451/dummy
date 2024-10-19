from num2words import num2words
import math
# name reverse by using words like name = "abc 123", ->>>>>>>> "123 abc"
name = "abc 123"
new_list = name.split()
print(new_list)

reverse_list = new_list[::-1]
print(reverse_list)

print(' '.join(reverse_list))       

# Convert from number to word
while True:
    try:
        user_number = int(input('Enter a number as your wish: '))
        break  # Exit the loop if input is valid
    except ValueError:
        print("That's not a valid number. Please try again.")
converted_number = num2words(user_number)
print(converted_number)       

# print prime numbers from a given range and also used function 
#checking prime number
def check_prime(number):
    temp = 0
    for i in range(2,number):
        if number % i == 0:
            temp = temp+1
    if temp>0:
        return False
    else:
        return True

#printing alternative prime number     
list_empty_prime = [] 
def print_prime_number(limit):
  
    for number in range(2,limit+1):
        if check_prime(number):
            list_empty_prime.append(number)
# Calling to this function             
print_prime_number(50)            

# Final result printing 
for data in range(0,len(list_empty_prime),2):
    print(list_empty_prime[data])            

# Find square root of a number without using sqrt() method
number = 16
guess = number/2.0

while True:
    new_guess = (guess+number/guess)/2.0
    if abs(new_guess-guess)<1e-10:
        break

    guess = new_guess

print(guess)    

#Direct Method to find out square root of a number
print(math.sqrt(number))


#Positive ,negative and neutral number in python 
number_1 = int(input('Enter a number'))
if number_1<0:
    print('Negative Number')
elif number_1==0:
    print('Neutral')
else:
    print('Positive Number') 

# Perfact square of a number 
number_2 = 27
sqrt = number_2 ** 0.5
if int(sqrt) ** 2 == number_2: 
 print('Perfact square') 
else:
    print('Not perfact square')


 # Print odd numbers from 1 to 100
for i in range(1,101):
  if i % 2 == 0:
      print(f"{i} is even number")
# Sum of Natural numbers in python       
sum=0
for i in range(1,101):
    sum = sum+i      
print(sum)

# Odd and Even numbers printing from a list
list_13 = [10,4,7,87,856,77]
for data in list_13:
    if data % 2 == 0:
        print(f'Even number {data}')
for data in list_13:
    if data % 2 != 0:
        print(f'Odd number {data}')

#Gcd 50,60 or HCF and LCM of given two numbers 
num1= 50
num2 = 60 
finalAnswer = 0
for i in range(1,num1+1):
  if num1 % i == 0 and num2 % i == 0:
      finalAnswer = i
print(f"HCF is {finalAnswer}")      
print(f"LCM is {(num1*num2)/finalAnswer}")