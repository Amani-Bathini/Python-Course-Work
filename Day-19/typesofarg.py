'''
#positional arg
def display(name,email,password):
  print(f'name:{name}')
  print(f'email:{email}')
  print(f'password:{password}')

display('xyz','xyz@gmail.com','xyz@123')
display('xyz@gmail.com','xyz','xyz@123')
display('xyz@123','xyz@gmail.com','xyz')
'''

'''
#keyword arg
def display(name,email,password):
  print(f'name:{name}')
  print(f'email:{email}')
  print(f'password:{password}')

display(name='xyz',email = 'xyz@gmail.com',password='xyz@123')
display(email='xyz@gmail.com',name='xyz',password='xyz@123')
display(password='xyz@123',email='xyz@gmail.com',name='xyz')
'''
'''
#default arg
def display(name,email='gmail.com',password=''):
  print(f'name:{name}')
  print(f'email:{email}')
  print(f'password:{password}')

display('xyz','xyz@gmail.com','xyz@123')
display('xyz','xyz@gmail.com')
display('xyz')
'''
'''
#variable length with positinal arg
def display(*names):
  print(names)

display('amani')
display('amani','anjana')
display('amani','anjana','reena')
display('amani','anjana','reena','akhila')
'''
'''
##variable length with keyword arg
def display(**products):
  print(products)

display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)
'''