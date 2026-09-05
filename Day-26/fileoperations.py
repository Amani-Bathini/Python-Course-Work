'''
file = open('pfs63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()
'''
'''
with open('pfs63.txt','r') as file:
  print(file.read())
  file.seek(0)
  print(file.readline())
  file.seek(0)
  print(file.readlines())
'''
'''
with open('pfs63.txt','w') as file:
  file.write("Shifted to Branch-1")
'''
'''
with open('pfs63.txt','a') as file:
  file.write("Only for today")
  '''
'''
with open('pfs63.txt','a+') as file:
  file.write("Tomorrow same branch-5")
  file.seek(0)
  print(file.read())
'''
'''
with open('pfs63.txt','w+') as file:
  file.write("Tom same branch-5")
  file.seek(0)
  print(file.read())
'''
'''
with open('pfs63.txt','r+') as file:
  file.write("Tomorrow same branch-5")
  file.seek(0)
  print(file.read())
'''