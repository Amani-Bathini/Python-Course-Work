Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,3,4,5,5]
l
[1, 2, 3, 4, 5, 5]
l.append(7)
l
[1, 2, 3, 4, 5, 5, 7]
l.insert(2,9)
l
[1, 2, 9, 3, 4, 5, 5, 7]
l.extend(10,11,12)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l.extend(10,11,12)
TypeError: list.extend() takes exactly one argument (3 given)
l.extend([10,11,12])TypeError: list.extend() takes exactly one argument (3 given)
SyntaxError: invalid syntax
l.extend([10,11,12])
l
[1, 2, 9, 3, 4, 5, 5, 7, 10, 11, 12]
l[2]=30
l
[1, 2, 30, 3, 4, 5, 5, 7, 10, 11, 12]
l.pop()
12
l.pop(4)
4
remove(10)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    remove(10)
NameError: name 'remove' is not defined
l.remove(4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l.remove(4)
ValueError: list.remove(x): x not in list
l.remove(10)
l
[1, 2, 30, 3, 5, 5, 7, 11]
l.clear()
l
[]
max(l)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    max(l)
ValueError: max() iterable argument is empty
l = [1,3,4,56,67,89,90]
max(l)
90
min(l)
1
sorted(l)
[1, 3, 4, 56, 67, 89, 90]
l
[1, 3, 4, 56, 67, 89, 90]
l=[90,89,56,3,2,5]
sorted(l)
[2, 3, 5, 56, 89, 90]
l
[90, 89, 56, 3, 2, 5]
l.reverse()
l
[5, 2, 3, 56, 89, 90]
l.sort()
l
[2, 3, 5, 56, 89, 90]
sum(l)
245
l=[1,2,3]
m=[1,2,3]
l
[1, 2, 3]
m
[1, 2, 3]
n = l
n
[1, 2, 3]
m = l.copy()
m.append(4)
l
[1, 2, 3]
m
[1, 2, 3, 4]
all
<built-in function all>
>>> all([0,' ',[],(),set(),{},False])
False
>>> all([1,'',[],(),{},False])
False
>>> any([1,'',[],(),{},False])
True
>>> sorted(l)
[1, 2, 3]
>>> l = [1,2,3,4]
>>> l.index(3)
2
>>> l.index(4)
3
>>> l.index(5)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l.index(5)
ValueError: 5 is not in list
>>> l.count(5)
0
>>> l.count(2)
1
>>> l = [[1,2,3,4],[5,6,7,8]]
>>> l
[[1, 2, 3, 4], [5, 6, 7, 8]]
>>> l[0]
[1, 2, 3, 4]
>>> l[1]
[5, 6, 7, 8]
>>> l[0][2]
3
>>> l[1][1]
6
>>> l[-1][-1]
8
>>> 
>>> t = ()
>>> t=tuple()
