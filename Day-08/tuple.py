Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t = ()
>>> t = tuple()
>>> t = (10,20,30)
>>> 
>>> t
(10, 20, 30)
>>> t(10,)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t(10,)
TypeError: 'tuple' object is not callable
>>> t = (10,)
>>> t
(10,)
>>> print(type(t))
<class 'tuple'>
>>> t = (10)
>>> t
10
>>> print(type(t))
<class 'int'>
>>> a = (1,2)
>>> b = (3,4)
>>> print(a+b)
(1, 2, 3, 4)
>>> print(a3)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(a3)
NameError: name 'a3' is not defined. Did you mean: 'a'?
>>> print(a*3)
(1, 2, 1, 2, 1, 2)
>>> print(a[0])
1
>>> print(b[1])
4
>>> t = (10,45,98,56)
>>> print(t[::])
(10, 45, 98, 56)
print(t[2:4])
(98, 56)
print(45 in t)
True
print(100 in t)
False
print(60 not in t)
True
print(98 in t)
True
print(76 in t)
False
t.len()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t.len()
AttributeError: 'tuple' object has no attribute 'len'
len((t))
4
max(t)
98
min(t)
10
sum(t)
209
sorted(t)
[10, 45, 56, 98]
any((0,0,1))
True
all((1,2,3))
True
t =(1,2,3,4,4,5,6)
t.count(4)
2
t.count()2
SyntaxError: invalid syntax
t.count(2)
1
t.index(2)
1
t = 10,20,30
print(t)
(10, 20, 30)
t =(10,20,30)
a,b,c = t
print(a)
10
print(b)
20
print(c)
30
data = ((1,2),(3,4))
data
((1, 2), (3, 4))
data = (10,[20,30],40)
data
(10, [20, 30], 40)
data[1].append(50)
print
<built-in function print>
print(data)
(10, [20, 30, 50], 40)
data[0] = 10
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    data[0] = 10
TypeError: 'tuple' object does not support item assignment
