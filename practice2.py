from num2words import num2words
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