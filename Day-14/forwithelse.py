'''
#else block will not execute when we break the iteration
for i in range(1,10):
  if i == 5:
    break
  print(i)
else:
  print("End of the Loop")
'''

'''
for i in range(1,10):
  if i == 4:
   print(i)
else:
  print("End of the Loop")
  '''


'''
pin = 1234
for _ in range(5):
  epin = int(input("Enter the Pin:"))
  if pin == epin:
    print("Unlock Phone")
    break
  else:
    print("Invalid pin")
else:
  print("Try After 30sec")
'''

'''
#FACTORS
n = int(input("Enter the number:"))
print("Factors: ",end=' ')
for i in range(1,n+1):
  if n % i == 0:
    print(i,end = ' ')
'''

'''
n = int(input("Enter the number:"))
print("Factors: ",end=' ')
c = 0
for i in range(1,n+1):
  if n % i == 0:
    c += 1
if c == 2:
  print("Prime number")
else:
  print("Not a prime number")
'''


'''
n = int(input("Enter the number:"))
for i in range(2,n//2+1):
  if n%i==0:
    print("not Prime number")
    break
else:
  print("Prime Number")
'''