Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count = 10
>>> count = 7
>>> count
7
>>> type(count)
<class 'int'>
>>> price = 6.5
>>> type(price)
<class 'float'>
>>> price
6.5
>>> c = (4+6j)
>>> c
(4+6j)
>>> c = (4+9J)
>>> c
(4+9j)
>>> type(c)
<class 'complex'>
>>> s = 'codegnan'
>>> type(s)
<class 'str'>
>>> s
'codegnan'
>>> l = []
>>> type(l)
<class 'list'>
>>> l = [1,2,4.5,'a',4+7j]
>>> l
[1, 2, 4.5, 'a', (4+7j)]
>>> t = ()
>>> type(t)
<class 'tuple'>
>>> t = (1,2,'asdfgh',5432)
>>> t
(1, 2, 'asdfgh', 5432)
>>> s = set()
>>> s={'monday','tuesday','wednesday','thursday'}
>>> type(s)
<class 'set'>
s = {1.1.1.1.1.1}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s = {1,1.1.1.1.1}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s = {1,1,1,1,1,1}
s
{1}
d = {'name':'amani','batch':63,'course':'PFS'}
d
{'name': 'amani', 'batch': 63, 'course': 'PFS'}
type(d)
<class 'dict'>
status = None
status
type(status)
<class 'NoneType'>
s=frozenset({1,2,3,4})
s
frozenset({1, 2, 3, 4})
