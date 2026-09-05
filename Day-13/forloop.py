'''
s = 'Python Programming'
for i in range(len(s)):
  if s[i] in 'aeiouAEIOU':
    print(i,s[i])
    '''

'''
l = [23,45,12,34,50,24,35,68,75,34,10]
sum = 0
for i in range(len(l)):
  if l[i]%2 == 0:
    sum = sum + i 
    print(i,l[i])
print(sum)
'''

'''
n = int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
  fact *= i
print(f"Factorial of {n} is {fact}")
'''

'''
data = {}
n = int(input("Enter the no. of students:"))
max_marks = 0
for i in range(n):
  name = input("Enter the name of student:")
  marks = int(input("Enter the marks of student:"))
  if marks > max_marks:
    max_marks = marks
  data[name] = marks

print(data)
print("Maximum Marks:",max_marks)
'''


products = {}
bill = 0
n = int(input("Enter the no. of products:"))
for i in range(n):
  product_name = input("Enter the product name:")
  price = int(input("Enter the price of product:"))
  quan = int(input("Enter the quantity of product:"))
  final_price = price * quan
  bill += final_price
  products[product_name] = f'{price} * {quan} = {final_price}'
print(products)
print("Total bill:",bill)