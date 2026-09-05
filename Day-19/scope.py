'''
def display(n):
  n = n+10   #local variable
  print("Inside:",n)
n = 10   #global variable
display(n)
print("Outside:",n)
'''
'''
def display():
  print("Inside:",n)
n=10
display()
print('Outside:',n)
'''
'''
def display():
  n = 10
  print('Inside:',n)
display()
print('Outside:',n)  #error
'''
'''
def display():
  global n 
  n = n+10
  print("Inside:",n)
n=10
display()
print("Outside:",n)
'''
'''
def display():
  global n
  n='PFS'
  print("Updsted Course:",n)
n='JFS'
display()
print("Final Course:",n)
'''
'''
def display():
  n = 'JFS'
  def update():
    nonlocal n  
    n = 'PFS'
    print("Updated Course:",n)
  update()
  print("Final Course:",n)
display()
'''
l=[1,2,3,4,5]
max = 20
sum = 10 #if we declare built-in function as var it acts as a var instead of function
print(sum)