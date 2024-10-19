from num2words import num2words
from itertools import permutations
import math,string
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

# Find total number of characters from a string
my_new_name = 'abcdef'
print(f"Length is {len(my_new_name)}")

l = 0
#OR
for i in my_new_name:
   l = l+1
print(l)

# Punctuations problem
count_punctuations = 0
my_new_punctuations_proble = 'moin@123&^%$#'
for item in my_new_punctuations_proble:
    if item in string.punctuation:
         count_punctuations = count_punctuations+1

print(f"Total number of puntuantions in this string {count_punctuations}")

# Vowels and Consonant 
vowel_consonant = "moin@123&^%$#"
count_vowels = 0
count_consonant = 0
count_special = 0
count_number = 0
for item_char in vowel_consonant:
    if item_char == 'a' or item_char == 'e' or item_char == 'i' or item_char == 'o' or item_char == 'u':
        count_vowels = count_vowels +1 
    elif item_char in string.punctuation:
        count_special = count_special+1
    elif item_char == '1' or item_char == '2' or item_char == '3' or item_char == '4' or item_char == '5' or item_char == '6' or item_char == '7' or item_char == '8' or item_char == '9' or item_char == '0': 
        count_number = count_number+1
    else:
        count_consonant = count_consonant +1    

print(f"total vowels are {count_vowels}")
print(f"total consonants are {count_consonant}") 
print(f"total specials are {count_special}")
print(f"total numbers are {count_number}")

# Anagrams of two strings 
str1 = input('Enter a string 1 ')
str2 = input('Enter a string 2 ')

str1 = str1.replace(' ','').lower()
str2 = str2.replace(' ','').lower()

if sorted(str1) == sorted(str2):
    print('Anagrams')
else:
    print('Not Anagrams')

# Possible number of permutations from a string 
permutations_string = "abc"
list_per = permutations(permutations_string)
per = 0    
for i in list_per:
    per = per+1
    print(' '.join(i))
print(f"Number of permutations are {per}")    