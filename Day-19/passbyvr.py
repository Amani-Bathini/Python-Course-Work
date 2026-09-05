#pass by value:passing the immutable items(int,float,str,tuple,bool) and it does  not effects outside the function
#pass by reference:passing mutable items(list,dict,set) and it effect the outside the function

'''
def display(n):
  n += 10
  print("Inside:",n)
n= 10
display(n)
print("Outside:",n)
'''
'''
def display(n):
  n += 10.5
  print("Inside:",n)
n= 10.9
display(n)
print("Outside:",n)
'''
'''
def display(n):
  n += " lang"
  print("Inside:",n)
n= "python"
display(n)
print("Outside:",n)
'''
'''
def display(n):
  n.append(12)
  print("Inside:",n)
n=[1,2,3,4]
display(n)
print("Outside:",n)
'''
'''
def display(n):
  n = (1,2,5)
  print("Inside:",n)
n= (1,2,3,4)
display(n)
print("Outside:",n)
'''
'''
def display(n):
  n = False
  print("Inside:",n)
n= True
display(n)
print("Outside:",n)
'''
'''
def display(n):
  n.add(8)
  print("Inside:",n)
n= {1,2,3,4}
display(n)
print("Outside:",n)
'''
def display(n):
  n[5]=6
  print("Inside:",n)
n={1:2,3:4}
display(n)
print("Outside:",n)