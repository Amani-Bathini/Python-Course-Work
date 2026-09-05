#Function calling itself untill it reaches the base condition

'''
def display(n):
  if n>10:
    return 
  print(n)
  display(n+1)
display(1)
'''
'''
def display(n):
   if n>10:
      return
   display(n+1)
   print(n)
display(1)
'''
'''
def displaysum(n):
  if n<1:
    return 0 
  return n+displaysum(n-1)

print(displaysum(8))
'''
'''
def displayprod(n):
  if n==0:
    return 1
  return n*displayprod(n-1)

print(displayprod(4))
'''
'''
def display(index):
    if index == len(s):
        return
    display(index + 1)
    print(s[index],end="")
s = "Python Programming"
display(0)
'''
'''
def display(n):
  if n == len(s)+1:
    return
  print(s[:n])
  display(n+1)

s= "Python"
display(1)
'''
'''
def display(ind,width):
  if ind > len(s)-width:
    return
  print(s[ind:ind+width])
  display(ind+1,width)

s="Python programming"
display(0,4)
'''
'''
def display(n):
  if n==0:
    return
  display(n//10)
  print(n%10,end="")
display(987654)
'''
'''
def display(n):
  if n==0:
    return 0
  return n%10 + display(n//10)
print(display(987654))
'''

  