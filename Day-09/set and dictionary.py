Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=set()
s={1,2,3,4,12,324,9876,34,12431324}
s
{1, 2, 3, 324, 4, 34, 12, 9876, 12431324}
s = {1,1,1,1,1,1}
s
{1}
l = {10,20,30}
m = {1,2,3,4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
m = {1,2,3,4}
l | m
{1, 2, 3, 20, 4, 10, 30}
l & m
set()
a = {1,2,3,4,5}
b = {3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
a ^ b
{1, 2, 4, 7, 9}
a >= (1,2)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a >= (1,2)
TypeError: '>=' not supported between instances of 'set' and 'tuple'
a>={1,2}
True
a>= {1,2,3,4}
True
a>={1,23,45}
False
a>= {3,4,5}
True
b >= {9,3}
True
b >= {3,5}
True
b >= {2.45.67}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b>={2,3,45,65}
False
2 <= a
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    2 <= a
TypeError: '<=' not supported between instances of 'int' and 'set'
2<=a
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    2<=a
TypeError: '<=' not supported between instances of 'int' and 'set'
{2} <= a
True
{1,2} <= q
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    {1,2} <= q
NameError: name 'q' is not defined
{{1,2}<=a
 {1,2}<=a
 
SyntaxError: '{' was never closed
{1,2}<=a
 
True
a.isdisjoint(b)
 
False
a.isdisjoint({9,10})
 
True
a.union(b)
 
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
 
{3, 5}
a.issuperset(b)
 
False
a
 
{1, 2, 3, 4, 5}
5 in a
 
True
10 in a
 
False
10 not in a
 
True
max(a)
 
5
min(a)
 
1
sorted(a)
 
[1, 2, 3, 4, 5]
sum(a)
 
15
a
 
{1, 2, 3, 4, 5}
b = a
 
b
 
{1, 2, 3, 4, 5}
b.add(12)
 
b
 
{1, 2, 3, 4, 5, 12}
a
 
{1, 2, 3, 4, 5, 12}
c=a.copy()
 
c.add(12)
 
c.add(13)
 
c
 
{1, 2, 3, 4, 5, 12, 13}
a
 
{1, 2, 3, 4, 5, 12}
a
 
{1, 2, 3, 4, 5, 12}
a.add(123)
 
a
 
{1, 2, 3, 4, 5, 123, 12}
a.update(14,18,10)
 
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.update(14,18,10)
TypeError: 'int' object is not iterable
a.update({14,18,10})
 
a
 
{1, 2, 3, 4, 5, 10, 12, 14, 18, 123}
a.pop()
 
1
a.pop()
 
2
a.pop()
 
3
a.remove(18)
 
a
 
{4, 5, 10, 12, 14, 123}
a.discard(8)
 
a.discard(123)
 
a
 
{4, 5, 10, 12, 14}
a.discard(123)
 
a.remove(123)
 
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.remove(123)
KeyError: 123
a = frozenset({11,12,13,10,10})
 
a
 
frozenset({10, 11, 12, 13})
d ={}
 
d=dict()
 
type(d)
 
<class 'dict'>
d = {'k1':'v1','k2':'v2','k3':'v3'}
 
id(d)
 
1364520543488
d['k4']='v4'
 
d
 
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d = {}
 
d[1]='int'
 
d
 
{1: 'int'}
d[12.3]='flt'
 
d
 
{1: 'int', 12.3: 'flt'}
d[2+5j]='comp'
 
d
 
{1: 'int', 12.3: 'flt', (2+5j): 'comp'}
d['abg']='str'
 
d
 
{1: 'int', 12.3: 'flt', (2+5j): 'comp', 'abg': 'str'}
d=[(1,2,3)]='tuple'
 
SyntaxError: cannot assign to literal
d=[(1,2,3,4)]='tuple'
 
SyntaxError: cannot assign to literal
d=[(2,3,4)]='tuple'
 
SyntaxError: cannot assign to literal
d[(1,2,3)]='tuple'
 
d
 
{1: 'int', 12.3: 'flt', (2+5j): 'comp', 'abg': 'str', (1, 2, 3): 'tuple'}
d['False']='bool'
 
d
 
{1: 'int', 12.3: 'flt', (2+5j): 'comp', 'abg': 'str', (1, 2, 3): 'tuple', 'False': 'bool'}
d[frozenset({1,2,3})]:'fset'
 
d
 
{1: 'int', 12.3: 'flt', (2+5j): 'comp', 'abg': 'str', (1, 2, 3): 'tuple', 'False': 'bool'}
d[frozenset({1,2,3})]='fset'
 
d
 
{1: 'int', 12.3: 'flt', (2+5j): 'comp', 'abg': 'str', (1, 2, 3): 'tuple', 'False': 'bool', frozenset({1, 2, 3}): 'fset'}
d={}
 
d[1]
 
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    d[1]
KeyError: 1
d[1]=1
 
d[2]=12.4
 
d[3]=12+4j
 
d[4]='str'
 
d[5]=[1,2,34,4]
 
d[6]=(1,2,3)
 
d[7]={1,2,3}
 
d[8]={1:1}
 
d[9]=True
 
d
 
{1: 1, 2: 12.4, 3: (12+4j), 4: 'str', 5: [1, 2, 34, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
9 in d
 
True
10 in d
 
False
>>> 'str' in d
...  
False
>>> d[5]
...  
[1, 2, 34, 4]
>>> d[8]
...  
{1: 1}
>>> d.get(9)
...  
True
>>> d.get(10)
...  
>>> d.get(10,'element is not present')
...  
'element is not present'
>>> d
...  
{1: 1, 2: 12.4, 3: (12+4j), 4: 'str', 5: [1, 2, 34, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
...  
>>> d
...  
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: [1, 2, 34, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=10
...  
>>> d
...  
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
...  
>>> d
...  
{1: 1, 2: 12.4, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
