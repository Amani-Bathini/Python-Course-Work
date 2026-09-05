Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> a=b=c=10
>>> a,b,c=10,20,30
>>> b
20
>>> a
10
>>> c
30
>>> a
10
>>> b
20
>>> a,b=b,a
>>> b
10
>>> a
20
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a
NameError: name 'a' is not defined
