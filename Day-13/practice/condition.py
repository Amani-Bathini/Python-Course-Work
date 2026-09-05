'''
#positive or neg
n = int(input("Enter a number:"))
if n >0:
  print("Number is positive")
else:
  print("Number is negative")
'''


'''
#even or odd
n = int(input("Enter a number:"))
if n % 2 == 0 :
  print("Number is Even")
else:
  print("Number is odd")
'''


'''
#divisible by 5
n = int(input())
if n % 5 == 0:
  print("given no. is divisible by 5")
else:
  print("given no. is not divisible by 5")
'''


'''
#divisible by 3 and 7
n = int(input("Enter a number:"))
if n % 3 == 0 and n % 7 == 0:
  print("given no. is divisible by 3 and 7")
else:
  print("Given no. is not divisible by 3 and 7")
'''


'''
#leap year
n = int(input("Enter a year:"))
if n % 4 == 0 or n % 400 == 0 and n % 100 != 0 :
  print("Year is leap year")
else:
  print("not a leap year")
'''

'''
#pass or fail
marks = int(input("Enter marks:"))
if marks >= 35:
  print("Pass")
else:
  print("Fail")
'''


'''
#checks if no. is 3 digit
num = abs(int(input("Enter a number: ")))
if num // 100 >= 1 and num // 1000 == 0:
    print("3-digit number")
else:
    print("Not a 3-digit number")
'''

'''
#checks if char is vowel
ch = input("Enter Character:")
if ch in 'aeiouAEIOU':
  print(f"{ch} is vowel")
else:
  print(f"{ch} is not a vowel")
'''

'''
#greatest of 2 num
num1 = int(input())
num2 = int(input())
if num1>num2:
  print (f"{num1} is greater")
else:
  print(f"{num2} is greater")
'''


'''
#smallest of 2 nums
num1 = int(input())
num2 = int(input())
if num1<num2:
  print (f"{num1} is smaller")
else:
  print(f"{num2} is smaller")
'''

'''
#checks if input is 0
n = int(input())
if n == 0:
  print("Number is zero")
else:
  print("Number is not zero")
'''

'''
#checks if a num is multiple of 10
num = int(input())
if num % 10 == 0:
  print("Multiple of 10")
else:
  print("Not multiple of 10")
'''


'''
#elgible to vote or not
age = int(input("Enter age:"))
if age>=18:
  print("eligible to vote")
else:
  print("not eligible to vote")
'''

'''
#checks if a no. btwn 1 and 100
n = int(input("Enter a number:"))
if n>1 and n < 99:
  print("In range")
else:
  print("Not in range")
'''


'''
#checks no. is square of another
num1 = int(input())
num2 = int(input())
if num1 == num2*num2:
  print(f"{num1} is square of {num2}")
'''

'''
#checks if 2 strings are equal
str1 = input()
str2 = input()
if str1 == str2:
  print("strings are equal")
else:
  print("strings are not equal")
'''

'''
#checks if a num is positive and even
num = int(input())
if num > 0 and num % 2 == 0:
  print("positive and even number")
'''


'''
#checks if a char is uppercase
chr = input()
if chr.isupper():
  print("Uppercase letter")
else:
  print("Not a uppercase")
'''

'''
#checks if temp is hot
temp = int(input())
if temp > 30:
  print("its hot")
'''

'''
#checks if a num is 4digit no,
num = int(input())
if num > 999 and num<9999 and num % 2==0:
  print("4 digit even number")
'''

'''
#checks if a chr is consonant
chr = input()
if chr not in 'aeiouAEIOU':
  print("Consonant")
'''

'''
#checks num is divisible by 2 or 3 but not both
num =int(input())
if num % 2 == 0 and num % 3 == 0:
  print("Divisible by 2 and 3")
elif num % 2 == 0:
  print("Divisible by 2 only")
elif num % 3 == 0:
  print("Divisible by 3 only")
else:
  print("Not Divisible by 2 or 3")
'''

'''
#checks if a num is neg and odd
num = int(input())
if num < 0 and num % 2 != 0:
  print("Negative and Odd")
'''

'''
#checks if a string starts with a vowel
str = input()
if str.lower().startswith(('a','e','i','o','u')):
  print("Starts with vowel")
else:
  print("Not starts with vowel")
'''


'''
#checks if 3 sides forms a valid triangle
s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
'''

'''
#greatest among 3 mem
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a, "is the greatest")
elif b >= a and b >= c:
    print(b, "is the greatest")
else:
    print(c, "is the greatest")
'''

'''
#checks if a year is century and leap
year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century Leap Year")
else:
    print("Not a Century Leap Year")
'''

'''
#check if a chr is digit
chr = input()
if chr.isdigit():
  print("Digit")
else:
  print("not a digit")
'''

'''
#checks whether a no. is palindrome
num = int(input("Enter a number: "))

temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
'''

'''
#compare len of 2 str
str1 = input()
str2 = input()
if len(str1) > len(str2):
  print(f"{str1} string is longer")
else:
  print(f"{str2} string is longer")
'''

'''
#checks if a no. is within a specific range(50 to 100) and divisible by 5
num = int(input("Enter a number: "))

if 50 <= num <= 100 and num % 5 == 0:
    print("The number is within the range and divisible by 5")
else:
    print("The number does not satisfy the condition")
'''

'''
#validate if a password len is str
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
'''

'''
#sum of 2 no. is even
num1 = int(input())
num2 = int(input())
sum = num1 + num2
if sum % 2 == 0:
  print("Sum is even")
else:
  print("Sum is not even")
'''

'''
#chr is spcl sym
chr = input()
if chr in ('!','@','#','etc'):
  print("Special symbol")
'''

'''
#checks temp is cold,moderate and hot
temp = int(input())
if temp < 15:
  print(" Cold")
elif temp>15 and temp< 30:
  print("Moderate")
elif temp>30:
  print("Hot")
'''

'''
#checks if a num is outside the range of 10 to 50
num = int(input())
if num > 10 and num > 50:
  print("Outside  range")
'''

'''
#perfect square
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i * i == num:
        print("Perfect Square")
        break
else:
    print("Not a Perfect Square")
'''

'''
#comparing 2 ages
age1 = int(input())
age2 = int(input())
if age1 > age2:
  print("First is Older")
elif age2>age1:
  print("Second is Older")
else:
  print("Both are same age")
'''

'''
#checks if an angle is acute ,right,obtuse
angle = int(input())
if angle == 90:
  print("Right Angle")
elif angle >0 and angle < 90:
  print("Acute Angle")
elif angle > 90 and angle<180:
  print("Obtuse Angle")
elif angle == 180:
    print("Straight Angle")
else:
    print("Invalid Angle")
'''


