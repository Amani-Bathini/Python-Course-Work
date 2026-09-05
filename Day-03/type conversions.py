Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> b = 10.5
>>> int(b)
10
>>> complex(b)
(10.5+0j)
>>> str(b)
'10.5'
>>> 
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c = (10+5j)
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+5j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s = 'codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'e', 'n', 'a', 'd', 'o', 'c', 'g'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
l = [1,2,'a','efgh']
int(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(1)
'1'
tuple(l)
(1, 2, 'a', 'efgh')
set(l)
{1, 2, 'a', 'efgh'}
dict(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t = (1,2,5,'asdf','kuyt')
int(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(t)
"(1, 2, 5, 'asdf', 'kuyt')"
list(t)
[1, 2, 5, 'asdf', 'kuyt']
set(t)
{1, 2, 'asdf', 5, 'kuyt'}
dict(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s = set()
s = {'mon','tues','wed','thurs','fri','sat'}
int(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
str(s)
"{'wed', 'mon', 'sat', 'fri', 'thurs', 'tues'}"
list(s)
['wed', 'mon', 'sat', 'fri', 'thurs', 'tues']
tuple(s)
('wed', 'mon', 'sat', 'fri', 'thurs', 'tues')
dict(s)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
bool(s)
True
d = {'name':'amani,'batch':63,'course':'PFS'}
     
SyntaxError: unterminated string literal (detected at line 1)
d = {'name':'amani','batch':63,'course':'PFS'}
     
int(d)
     
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
     
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
     
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(d)
     
"{'name': 'amani', 'batch': 63, 'course': 'PFS'}"
list(d)
     
['name', 'batch', 'course']
tuple(d)
     
('name', 'batch', 'course')
set(d)
     
{'course', 'batch', 'name'}
bool(d)
     
True
a = True
     
int(a)
     
1
float(a)
     
1.0
complex(a)
     
(1+0j)
str(a)
     
'True'
list(a)
     
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
tuple(a)
     
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
set(a)
     
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
dict(a)
     
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
