Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c = 'python programming'
len(c)
18
ord('p')
112
ord('A')
65
ord('C')
67
chr(65)
'A'
chr('D')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    chr('D')
TypeError: 'str' object cannot be interpreted as an integer
chr(78)
'N'
chr(66)
'B'
min(c)
' '
max(c)
'y'
sort(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sort(c)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c = 'String is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.Capitalize()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c.Capitalize()
AttributeError: 'str' object has no attribute 'Capitalize'. Did you mean: 'capitalize'?
c.capitalized()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c.capitalized()
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
'STRRAEMA'.casefold()
'strraema'
c.center(60,'o')
'ooooooooooooooooooooString is immutableooooooooooooooooooooo'
c.center(60,'*')
'********************String is immutable*********************'
s.ljust(60,'o')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.ljust(60,'o')
NameError: name 's' is not defined
c.ljust()60,'0')
SyntaxError: unmatched ')'
c.ljust(6-,'0')
SyntaxError: invalid syntax
c.ljust(60,'-')
'String is immutable-----------------------------------------'
c.rjust(60,'+')
'+++++++++++++++++++++++++++++++++++++++++String is immutable'
'12'.zfill(4)
'0012'
'458'.zfill(5)
'00458'
"12345".zfill(5)
'12345'
c.find('i')
3
c.find('b')
16
c.rindex('i')
10
c.rfind('i')
10
s.find(z)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.find(z)
NameError: name 's' is not defined
c.find('z')
-1
c.index('z')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c.count('i')
3
c.count('s')
1
c.replace('i','0')
'Str0ng 0s 0mmutable'
s.replace('String','Float')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.replace('String','Float')
NameError: name 's' is not defined
c.replace('String','Float')
'Float is immutable'
s.maketrans('aeiou','12345')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.maketrans('aeiou','12345')
NameError: name 's' is not defined
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
c.split()
['String', 'is', 'immutable']
'String,is,immutable'.split()
['String,is,immutable']
'String,is,immutable'.split(',')
['String', 'is', 'immutable']
'String,is,immutable'.rsplit()
['String,is,immutable']
'String,is,immutable'.split(,1)
SyntaxError: invalid syntax
'String,is,immutable'.split('',1)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    'String,is,immutable'.split('',1)
ValueError: empty separator
'String,is,immutable'.rsplit(',',1)
['String,is', 'immutable']
'String,is,immutable'.split(',',1)
['String', 'is,immutable']
'''
python
programming
language
'''
'\npython\nprogramming\nlanguage\n'
s.splitline()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.splitline()
NameError: name 's' is not defined
c.splitlines()
['String is immutable']
s = '''
python
programming
language
'''
s
'\npython\nprogramming\nlanguage\n'
s.splitlines()
['', 'python', 'programming', 'language']
''.join(['', 'python', 'programming', 'language'])
'pythonprogramminglanguage'
'-'.join(['', 'python', 'programming', 'language'])
'-python-programming-language'
','.join([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    ','.join([1,2,3,4])
TypeError: sequence item 0: expected str instance, int found
','.join(['1,2,3,4'])
'1,2,3,4'
'python.py'.partition('.')
('python', '.', 'py')
s = "java,pyhton,c,c++"
s.prtiton
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.prtiton
AttributeError: 'str' object has no attribute 'prtiton'. Did you mean: 'partition'?
>>> s.partition(',')
('java', ',', 'pyhton,c,c++')
>>> s.rpartition(',')
('java,pyhton,c', ',', 'c++')
>>> s.lpartiton(',')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.lpartiton(',')
AttributeError: 'str' object has no attribute 'lpartiton'. Did you mean: 'partition'?
>>> s.lpartition(',')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.lpartition(',')
AttributeError: 'str' object has no attribute 'lpartition'. Did you mean: 'partition'?
>>> c = 'Hello world'
>>> c.strip()
'Hello world'
>>> c.strip()
'Hello world'
>>> c = '                   hello        world   '
>>> c
'                   hello        world   '
>>> c.strip()
'hello        world'
>>> c.strip()
'hello        world'
>>> c.strip()
'hello        world'
>>> c.rstrip()
'                   hello        world'
>>> c.lstrip()
'hello        world   '
>>> text = "Hello "
>>> text.encode()
b'Hello '
>>> b'Hello '.decode()
'Hello '
