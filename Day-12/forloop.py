 #str,list,tuple,dict,set,range()
'''
for var in seq:
   print(var)
   range:seq of steps to generate numeric values
'''

'''
s = 'Codegnan'
for ch in s:
  if ch in 'aeiouAEIOU':
    print(ch)
'''

'''
l = [10,2,3,20,45,30,76,45,8,6]
for i in l:
  if i%2==0:
    print(i,"Even")
  else:
    print(i,"Odd")
'''

'''
marks =(90,85,30,45,60,20,47,10)
for mark in marks:
  if mark > 35:
    print(mark,"Pass")
  else:
    print(mark,"Fail")

'''

'''
followers = {'anjana','amani','akhila','sri','archu'}
for i in followers:
  print(i)
'''

'''
bus = {'s1':'Booked','s2':'Available','s3':'Available','s4':'Booked','s5':'Available'}
for seat in bus:
  if bus.get(seat) == 'Available':
    print(seat,"Available")
'''

'''
for i in range(1,11):
  print(i)
'''

'''
for i in range(10,0,-1):
  print(i)
'''

'''
for i  in range(2,51,2):
  print(i)
'''

'''
for i in range(1,100,3):
  print(i)
  '''
'''
for i in range(1,100,2):
  print(i,end=" ")

'''

'''
for i in range(5,51,5):
  print(i)
'''

n = int(input("Enter the table no.:"))
for i in range(1,11):
  print(f"{n} * {i} = {n*i}")