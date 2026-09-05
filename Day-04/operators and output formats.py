Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 20
a
20
b = 10
a+b
30
a-b
10
a
20
a*b
200
a/b
2.0
9/4
2.25
a//b
2
9//4
2
a%b
0
9%4
1
a**2
400
b**2
100
a<b
False
a>b
True
a<=b
False
a>=b
True
a == b
False
a!=b
True
c = 10
c = c+10
c += 10
c
30
c -= 10
c
20
c * = 2
SyntaxError: invalid syntax
c *= 2
c
40
c /= 2
c
20.0
c %= 3
c
2.0
c /= 1
c
2.0
c ** = 2
SyntaxError: invalid syntax
c **=2
c
4.0
n = 10
n % 2 == 0
True
n  %2== 0 and n%3 == 0
False
n % 2 == 0 or n%3 == 0
True
n
10
n<5
False
not n<5
True
s = 'codegnan'
'e' in s
True
'z' in s
False
'f' not in a
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    'f' not in a
TypeError: argument of type 'int' is not iterable
't' not in a
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    't' not in a
TypeError: argument of type 'int' is not iterable
'f' not in s
True
't' not in s
True
l = [1,2,3,4]
4 in l
True
5 in l
False
5 not in l
True
t = (1,2,3,4,5,5,6)
3 in t
True
4 in t
True
6 not in t
False
9 in t
False
9 not in t
True
set = {1,2,3,4,5,6}
7 in a
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    7 in a
TypeError: argument of type 'int' is not iterable
7 in s
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    7 in s
TypeError: 'in <string>' requires string as left operand, not int
7 in set
False
10 in set
False
8 in set
False
6 in set
True
9 not in set
True
d = {'name':'amani','batch':63,'course':python}
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d = {'name':'amani','batch':63,'course':python}
NameError: name 'python' is not defined
d = {'name':'amani','batch':63,'course':'python'}
name in d
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
'name' in d
True
'amani' in d
False
'batch' in d
True
63 in d
False
'python' in d
False
'course' in d
True
l = [1,2,3,4]
m = [1,2,3,4]
id(l)
2838700569472
id(m)
2838700464896
n = l
id(n)
2838700569472
l is n
True
i is not n
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    i is not n
NameError: name 'i' is not defined. Did you mean: 'id'?
l is not n
False
l is not m
True
s = 'codegnan'
id(s)
2838700570672
s = 'codegnan course'
s
'codegnan course'
id(s)
2838700674288
set = {1,2,3,4,5}
s.append(6)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.append(6)
AttributeError: 'str' object has no attribute 'append'
set.append(6)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    set.append(6)
AttributeError: 'set' object has no attribute 'append'
id(set)
2838695256896
set = {1,2,3,4,5,6,7,8}
s
'codegnan course'
set
{1, 2, 3, 4, 5, 6, 7, 8}
id(set)
2838700376576
set.add(9)
set
{1, 2, 3, 4, 5, 6, 7, 8, 9}
id(set)
2838700376576
9 & 10
8
9 | 10
11
9^10
3
8>>2
2
8<<2
32
s = 'codegnan'
b = `0.5
SyntaxError: invalid syntax
a = 10
b = 10.5
c ='codegnan'
print(a,b,c)
10 10.5 codegnan
print("a value is:",a)
a value is: 10
print("print b value is:",b)
print b value is: 10.5
print("c value is:",c)
c value is: codegnan
print(a,b,c,sep='')
1010.5codegnan
print(a,b,c,sep='\n')
10
10.5
codegnan
print(a,b,c,sep='\t')
10	10.5	codegnan
print(a,b,c.sep='\t',end='@')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
print(a,b,c,sep='\t',end='@')
10	10.5	codegnan@
print(a,b,c,sep='\t',end=\n\n')
      
SyntaxError: unexpected character after line continuation character
print(a,b,c,sep='\t',end='\n\n')
      
10	10.5	codegnan

>>> print(f"a ={a] b = {b} c = {c}")
...       
SyntaxError: f-string: unmatched ']'
>>> print(f"a ={a} b = {b} c = {c}")
...       
a =10 b = 10.5 c = codegnan
>>> print(a = %d,b=%f,c=%f)
...       
SyntaxError: invalid syntax
>>> print(a =%d,b=%f,c=%f)
...       
SyntaxError: invalid syntax
>>> print('a =%d,b=%f,c=%f')
...       
a =%d,b=%f,c=%f
>>> print(a =%d,b=%f,c=%s)
...       
SyntaxError: invalid syntax
>>> print("a =%d,b=%f,c=%s"%(a,b,c))
...       
a =10,b=10.500000,c=codegnan
>>> print('a={} | b={} | c={}',format()a,b,c))
SyntaxError: unmatched ')'
>>> print('a={} | b={} | c={}',format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    print('a={} | b={} | c={}',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> print('a={} | b={} | c={}'.format()a,b,c))
SyntaxError: unmatched ')'
>>> print('a={} | b={} | c={}'.format(a,b,c))
a=10 | b=10.5 | c=codegnan
>>> print('a={1} | b={2} | c={0}'.format)a,b,c))
SyntaxError: unmatched ')'
>>> print('a={1} | b={2} | c={0}'.format(a,b,c))
a=10.5 | b=codegnan | c=10
