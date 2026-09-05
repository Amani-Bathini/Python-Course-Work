'''
1#Print Numbers from 1 to N
n = int(input("Enter a number:"))
for i in range(1,n+1):
  print(i)
'''

'''
2#Print Even Numbers from 1 to N
n = int(input("Enter a number:"))
for i in range(2,n+1,2):
  print(i)
'''

'''
3#Sum of Numbers from 1 to N
n = int(input("Enter a number:"))
sum = 0 
for i in range(1,n+1):
  sum += i
print(sum)
'''

'''
4#Print Odd Numbers from 1 to N
n = int(input("Enter a number:"))
for i in range(1,n+1,2):
  print(i)
'''

'''
5#Find Factorial of a Number
n = int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
  fact = fact*i
print(fact)
'''

'''
6#Print Multiplication Table of N
n = int(input("Enter a number:"))
for i in range(1,11):
  print(f"{n}*{i} = {n*i}")
'''

'''
7#Check Prime Number
n = int(input("Enter the number:"))
for i in range(2,n//2+1):
  if n%i==0:
    print("not Prime number")
    break
else:
  print("Prime Number")
'''

'''
8#Sum of Digits of a Number
n = int(input("Enter a number:")) 
sum = 0
while n > 0:  
  digit = n%10  
  sum += digit  
  n = n//10     
print(sum)
'''

'''
10#Count Numbers Divisible by 3 (Using for loop)
n = int(input("Enter a number:"))
count = 0
for i in range(1,n+1):
  if i % 3 == 0:
    count +=1
print(count)
'''


'''
11#palindrome
n = int(input("Enter a number"))
temp = n
rev = 0
while n >0:
  digit = n % 10
  rev = rev * 10 + digit
  n = n//10
if temp == rev:
  print("Palindrome")
else:
  print("not a palindrome")
'''

'''
19#Print Numbers Divisible by Both 3 and 5
n = int(input())
for i in range(1,n+1):
  if i%3 == 0 and i % 5 == 0:
    print(i)
'''

'''
18#Product of Digits of a Number
n = int(input("Enter a number:"))
prod = 1
while n > 0:
  digit = n % 10
  prod = prod*digit
  n = n//10
print(prod)
'''

'''
16#Print Numbers from N to 1
n = int(input("Enter a number:"))
while n>=1:
  print(n)
  n = n-1
'''

'''
15#Sum of First N Natural Numbers
n = int(input("Enter n:"))
sum=0
for i in range(1,n+1):
  sum = sum+i
print(sum)
'''

'''
12#Print Multiples of 5 up to N (Using for loop)
n = int(input("Enter a number:"))
for i in range(1,n+1):
  if i % 5 == 0:
    print(i)
'''