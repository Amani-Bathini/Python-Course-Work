'''
username = input("username:")
password = input("password:")

if username == "admin" and password == "admin123":
    print("Login successful!")
else:
    print("Invalid credentials.")
    '''
'''
products = ['Laptop','Mobile','Watch']
search = input("Search Product")
if search in products:
    print("Product Found")
else:
    print("Product not found")
    '''

bill = int(input("Enter the bill:"))
if bill>99:
    print(bill)
else:
    print(bill+30)