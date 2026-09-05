Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = input()
asdfgh
>>> x
'asdfgh'
>>> name= input()
amani
>>> name
'amani'
>>> name = input("Enter your name:")
Enter your name:amani
>>> name
'amani'
>>> age = input("Enter the age")
Enter the age21
>>> age
'21'
>>> type(age)
<class 'str'>
>>> age = int(input("Enter your age"))
Enter your age21
>>> age
21
>>> type(age)
<class 'int'>
>>> names = input("Enter the names:")
Enter the names:amani akhila abhi
>>> names
'amani akhila abhi'
>>> names.split()
['amani', 'akhila', 'abhi']
>>> names = input(""Enter the names:").split()
...               
SyntaxError: unterminated string literal (detected at line 1)
>>> names = input("Enter the names:").split()
...               
Enter the names:amani akhila abhi
names
              
['amani', 'akhila', 'abhi']
names = input("Enter your names").split()
              
Enter your names1 2 3 4 5 6
names
              
['1', '2', '3', '4', '5', '6']
map(int,names)
              
<map object at 0x000001830884B910>
list(map(int,names))
              
[1, 2, 3, 4, 5, 6]
values = list(map(int,input().split()))
              
1 2 3 4  567
values
              
[1, 2, 3, 4, 567]
names = tuple(input("Enter the names:").split())
              
Enter the names:amani akhila abhi
names
              
('amani', 'akhila', 'abhi')
values = tuple(map(int,input("Enter the values").split()))
              
Enter the values1 2 3 4 45 67  890
values
              
(1, 2, 3, 4, 45, 67, 890)
values = tuple(map(float("Enter values").split()))
              
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    values = tuple(map(float("Enter values").split()))
ValueError: could not convert string to float: 'Enter values'
KeyboardInterrupt
values = tuple(map(float,input("Enter values").split()))
              
Enter values 2.3 4.5 6.7
values
              
(2.3, 4.5, 6.7)
names = set(input().split())
              
amani akhila abhi
names
              
{'abhi', 'amani', 'akhila'}
values = set(map(int,input().split()))
              
1 2 3 44 556 
values
              
{1, 2, 3, 44, 556}
values = set(map(float,input().split()))
              
1 2.3 3.6
values
              
{1.0, 2.3, 3.6}
email,password = input("Enter the  email and password:").split()
              
Enter the  email and password:amani@gmail.com 12345
email
              
'amani@gmail.com'
password
              
'12345'
a,b,c = list(map(int,input().split()))
              
1 2 3
a
              
1
b
              
2
c
              
3
names ,marks = input().spli()
              
amani 20
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    names ,marks = input().spli()
AttributeError: 'str' object has no attribute 'spli'. Did you mean: 'split'?
names ,marks = input().split()
              
amani 30
name
              
'amani'
marks
              
'30'
int(marks)
              
30
type(marks)
              
<class 'str'>
type(marks)
              
<class 'str'>
e = eval(input())
              
1
e
              
1
e = eval(input())
              
1.2
e
              
1.2
e = eval(input())
              
amani
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    e = eval(input())
  File "<string>", line 1, in <module>
NameError: name 'amani' is not defined
e = eval(input())
              
"amani"
e
              
'amani'
e = eval(input())
              
[1,2,3,4]
e
              
[1, 2, 3, 4]
e = eval(input())
              
(1,2,3,4,4)
e
              
(1, 2, 3, 4, 4)
e = eval(input())
              
{1,2,3,4}
e
              
{1, 2, 3, 4}
e = eval(input())
              
{1:'a',2:'b'}
e
              
{1: 'a', 2: 'b'}
e = eval(input())
              
True
e
              
True
