# # User input in python 
# # name = input("Enter your name :")
# # print("My name is ",name)

# # age = int(input("Enter your age ")) # age is integer and input function returs string , so we have to type convert from str to int
# # print("My age is ",age)

# # marks = float(input("Enter your marks "))
# # print(marks)

# # name = input("Enter your name :")
# # print("my name is ",name)

# # age = int(input('Enter your age'))
# # print('my age is',age )

# # marks = float (input("Enter your marks"))
# # print(marks)

# list = ['mohiz','ahan']

# print(list)

# for name in list:
#     print(name)

# res = list[1]
# print(res)

# list.append('nufair')

# print(list)

# list.remove('ahan')

# print('ahan')



# #range(7)# 0 1 2 3 4 5 6 




# for values in range(7):
#     print(values," ")
#     print()

# for values in range( 1,18):
# #     print(values,)


# # for data in range(3,19):

# #     print(data," ")



# # for data in range(0,39,3):

#     # print(data)
    
# list =['mohis']

# print(list)

# for name in list : 
#     print(name)

# res = list[0]

# print(res)

# list.append('aahil')

# print(list)

# list.remove('aahil')

# print(list)

#list of numbers 
list_numbers = [10,40,77,50,7]

for numbers in list_numbers:
    if numbers == 77:
        print("Moise")
    
print()
#sorting  the list
print("Sorting list in ascending order")
list_numbers.sort()        
for d in list_numbers:
    print(d)         


#attendence of list 
list_student_attendence = ['present','absent']

name_moise = ''
name_moise = list_student_attendence[0]
for attendence in list_student_attendence:
    if attendence == name_moise:
        print("Moise is present")
   
