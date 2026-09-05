'''
#students details display
def display(name,email,password):
  print(f"Hello {name},")
  print(f"Your Email: {email}")
  print(f"Your Paaword: {password}")


display('Amani','amanibathini@gmail.com','amani123')
display('Akhila','akhilabathini@gmail.com','akhi123')
display('Abhi','abhi@gmail.com','abhi123')
'''

'''
#checks leap year or not
def isleapyear(year):
  if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    print(f"{year} is leap year")
  else:
    print(f"{year} is not leap year")

for year in range(2000,2027):
 isleapyear(year)
'''

'''
#sum of digits
def sumofdigits(n):
  sum = 0
  while n>0:
    sum+= n%10
    n = n//10
  return sum

n = int(input("Enter the number:"))
print(f"sum of {n} digits is {sumofdigits(n)}")
'''

'''
#product of digits
def prodofdigits(n):
  prod = 1
  while n>0:
    prod *= n%10
    n = n//10
  return prod

n = int(input("Enter the number:"))
print(f"product of {n} digits is {prodofdigits(n)}")
'''

'''
#strong password or not
def checkpassword(password):
  if len(password)>0:
    check = set()
    for i in password:
      if i.isupper():
        check.add('u')
      elif i.islower():
        check.add('l')
      elif i.isdigit():
        check.add('d')
      else:
        check.add('s')
    if len(check) == 4:
      return "Strong Password"
  return "weak password"

p = input("Enter the password") 
print(f"Password is {checkpassword(p)}")
'''

#tables printing using funtn
def table(n):
  print(f"-----------Table-{n}---------------")
  for i in range(1,11):
    print(f"{n} * {i} = {n * i} ")

for i in range(1,21):
  table(i)