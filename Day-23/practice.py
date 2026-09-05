'''
#Create a list containing numbers from 1 to 20 using list comprehension.
l = [i for i in range(1,11)]
print(l)
'''
'''
#Create a list containing the squares of numbers from 1 to 10.
n = list(map(int,input().split()))
l = [i**2 for i in n]
print(l)
'''
'''
#Create a list containing the cubes of numbers from 1 to 10.
n = list(map(int,input().split()))
l = [i**3 for i in n]
print(l)
'''
'''
#Extract all even numbers from a given list.
n = list(map(int,input().split()))
l = [i for i in n  if i%2 == 0]
print(l)
'''
'''
#Extract all odd numbers from a given list.
n = list(map(int,input().split()))
l = [i for i in n  if i%2 != 0]
print(l)
'''
'''
#Convert all words in a list to uppercase.
l = input().split()
res = [word.upper() for word in l]
print(res)
'''
'''
#Convert all words in a list to lowercase.
l = input().split()
res = [word.lower() for word in l]
print(res)
'''
'''
#Extract all numbers greater than 10 from a list.
n = list(map(int,input().split()))
l = [i for i in n  if i>10]
print(l)
'''
'''
#Extract all numbers less than 10 from a list.
n = list(map(int,input().split()))
l = [i for i in n  if i<10]
print(l)
'''
'''
#Extract all numbers divisible by 5.
n = list(map(int,input().split()))
l = [i for i in n  if i%5==0]
print(l)
'''
'''
#Extract all positive numbers from a list.
n = list(map(int,input().split()))
l = [i for i in n  if i>0]
print(l)
'''
'''
#Extract all negative numbers from a list.
n = list(map(int,input().split()))
l = [i for i in n  if i<0]
print(l)
'''
'''
#Create a list containing the length of every word.
l = input().split()
res = [len(word) for word in l]
print(res)
'''
'''
#Extract all vowels from a given string.
l = input()
res = [i for i in l if i in ('a','e','i','o','u','A','E','I','O','U')]
print(res)
'''
'''
#Extract words that start with the letter "p".
l = input().split()
res = [word for word in l if word.startswith("p")]
print(res)
'''
'''
#Extract words having more than 5 characters.
l = input().split()
res = [word for word in l if len(word)>5]
print(res)
'''
'''
#Add 10 to every number in a list.
n = list(map(int,input().split()))
l = [i+10 for i in n]
print(l)
'''
'''
#Multiply every number in a list by 2.
n = list(map(int,input().split()))
l = [i*2 for i in n]
print(l)
'''
'''
#Replace every negative number with 0.
n = list(map(int,input().split()))
l = [i if i>0 else 0 for i in n]
print(l)
'''
'''
#Create a list containing "Even" or "Odd" for every number.
n = list(map(int,input().split()))
l = ["Even" if i%2==0 else "Odd" for i in n]
print(l)
'''
'''
#21. Find common elements between two lists using list comprehension.
n = list(map(int,input().split()))
m = list(map(int,input().split()))
l = [i  for i in n if i in m]
print(l)
'''
'''
#Find numbers divisible by both 3 and 5.
l = [i for i in range(1,61)  if i%3 == 0 and i%5 == 0]
print(l)
'''
'''
#Reverse every word in a list using list comprehension.
l = input().split()
res = [word[::-1] for word in l ]
print(res)
'''
'''
#Extract the first character of every word.
l = input().split()
res = [word[0] for word in l ]
print(res)
'''
'''
#Convert a list of string numbers into integers.
l= input().split()
res = [int(n) for n in l ]
print(res)
'''
'''
#Flatten a nested list using list comprehension.
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

res = [num for i in l for num in i]
print(res)
'''
'''
#Create a list of tuples containing each number and its square.
n = list(map(int,input().split()))
res = [(i,i**2) for i in n]
print(res)
'''
'''
#Extract words containing the letter "a".
l = input().split()
res = [word for word in l if "a" in word]
print(res)
'''
'''
#Create a multiplication table using nested list comprehension.
n=int(input())
m=int(input())
res = [[i * j for j in range(1, m + 1)] for i in range(1, n + 1)]

print(res)
'''

#Find all prime numbers from a given range using list comprehension.
n = int(input())
res = [i for i in range(n+1) if i%i == 0]