# Star patterns in python 

print('+++++++++++++++++++++++++++++++++')
print('Problem 1 ')
print()
for i in range(5):
   for j in range(5):
      if j<=i:
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print()


print()
print('+++++++++++++++++++++++++++++++++')
print('Problem 2 ')
print()

for i in range(5):
   for j in range(5):
      if j>=4-i:
         print('*',end=' ')
      else:
         print(' ',end=' ') 
   print()      




print('+++++++++++++++++++++++++++++++++')
print('Problem 3 ')
print()

for i in range(1,6):
   for j in range(1,6):
      if j>=i:
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print() 


print('+++++++++++++++++++++++++++++++++')
print('Problem 4 ')
print()

for i in range(1,6):
   for j in range(1,6):
     
      if j<=6-i:
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print()            


print('+++++++++++++++++++++++++++++++++')
print('Problem 5 ')
print()   



for i in range(1,6):#output         
   for j in range(1,10):
      if j>=6-i and j<=i+4:# 5 
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print()      

print('+++++++++++++++++++++++++++++++++')
print('Problem 6 ')
print()   

k=True
for i in range(1,6):
   for j in range(1,10):
      if j>=6-i and j<=4+i and k == True:
         print('*' ,end=' ')
         k = False
      else:
         print(' ',end=' ')
         k = True
   print()         

print('+++++++++++++++++++++++++++++++++')
print('Problem 7 ')
print()

for i in range(1,6):
   for j in range(1,10):
      if j<=6-i or j>=4+i:
         print('*',end=' ')
      else:
         print(' ',end=' ')   
   print()      

print('+++++++++++++++++++++++++++++++++')
print('Problem 8 ')
print()



for i in range(1,5):
   char = 'A'
   for j in range(1,8):
      if j<=5-i or j>=3+i:
         print(char,end=' ')
         if j<4:
 
            char = chr(ord(char) + 1)
         else:
            char = chr(ord(char) - 1)
            
      else:
         print(' ',end=' ')
    
   print()         

print('+++++++++++++++++++++++++++++++++')
print('Problem 9 ')
print()

k = 0
for i in range(1,8):
   if i<=4:
      k+=1
   else:
      k-=1   
   for j in range(1,8):
      if j>=5-k and j<=k+3:
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print()         


print('+++++++++++++++++++++++++++++++++')
print('Problem 10 ')
print()

k=0
for i in range(1,8):
   if i<=4: 
      k+=1 
   else:
      k-=1 
   
   for j in range(1,5):
      if j<=k:
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print()    

print('+++++++++++++++++++++++++++++++++')
print('Problem 11 ')
print()

for i in range(1,5):
   for j in range(1,8):
      if j>=i and j<=8-i:
         print('*',end=' ')
      else:
         print(' ',end=' ')
   print()      

print('+++++++++++++++++++++++++++++++++')
print('Problem 12 ')
print()


k=0
for i in range(1,8):
   k=i
   for j in range(1,8):

      if j<=8-k:
         print('*',end=' ')
         
      else:
         print(' ',end=' ')
   print()      