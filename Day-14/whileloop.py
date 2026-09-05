'''
i = 1
while i<=10:
  print(i)
  i += 1
'''

'''
i = 10
while i>0:
  print(i)
  i -= 1
'''

'''
i=2
while i<=100:
  print(i,end=',')
  i += 2
'''

'''
s ='python programming'
i=len(s)-1
while i>=0:
  print(s[i],end='')
  i -= 1
'''

'''
l = [1,0,0,0,2,3,4,5,56,12,0,12,0,13,0,0,16,0]
while 0 in l:
  l.remove(0)
print(l)
'''

'''
d={}
totalbill = 0
while True:
   pn= input("Enter productname(for exit):")
   if pn == 'exit':
      break
   price = int(input("Enter price"))
   totalbill += price
   d[pn] = price
   
print(d)
print("TotalBill:",totalbill)
'''

i =0 
while i<10:
  i+=1
  if i == 15:
    break

else:
  print("End of the loop")

  8,9,11,14,17,20