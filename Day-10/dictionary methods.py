Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={'name':'amani','batch':63,'course':'PFS'}
>>> data['name']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data['name']
NameError: name 'data' is not defined
>>> d['name']
'amani'
>>> d['batch']
63
>>> d['course']
'PFS'
>>> 63 in d
False
>>> d['age']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d['age']
KeyError: 'age'
>>> d.get('age','key is not present')
'key is not present'
>>> d.get('batch'.'key is not present')
SyntaxError: invalid syntax
>>> d.get('batch','key is not present')
63
>>> data['branch']=64
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data['branch']=64
NameError: name 'data' is not defined
>>> d['branch']=64
>>> d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64}
>>> s['skills']=['python','mysql','flask']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s['skills']=['python','mysql','flask']
NameError: name 's' is not defined
d['skills']=['python','mysql','flask']
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask']}
d['agw']=21
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'agw': 21}
d.update(['phno.':1234566790,'email':'amani@gmail.com'])
SyntaxError: invalid syntax
d.update(['phno':1234566790,'email':'amani@gmail.com'])
SyntaxError: invalid syntax
d.update({'phno':1234566790,'email':'amani@gmail.com'})
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'agw': 21, 'phno': 1234566790, 'email': 'amani@gmail.com'}
d.pop('age')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d.pop('age')
KeyError: 'age'
d.pop('agw')
21
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'phno': 1234566790, 'email': 'amani@gmail.com'}
d.pop('email')
'amani@gmail.com'
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'phno': 1234566790}
d.popitem()
('phno', 1234566790)
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask']}
d.popitem()
('skills', ['python', 'mysql', 'flask'])
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64}
d.clear()
d
{}
d={'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'agw': 21, 'phno': 1234566790, 'email': 'amani@gmail.com'}
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'agw': 21, 'phno': 1234566790, 'email': 'amani@gmail.com'}
d.key()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
d.keys()
dict_keys(['name', 'batch', 'course', 'branch', 'skills', 'agw', 'phno', 'email'])
d.values()
dict_values(['amani', 63, 'PFS', 64, ['python', 'mysql', 'flask'], 21, 1234566790, 'amani@gmail.com'])
d.items()
dict_items([('name', 'amani'), ('batch', 63), ('course', 'PFS'), ('branch', 64), ('skills', ['python', 'mysql', 'flask']), ('agw', 21), ('phno', 1234566790), ('email', 'amani@gmail.com')])
sorted(d)
['agw', 'batch', 'branch', 'course', 'email', 'name', 'phno', 'skills']
sorted(d,reverse=True)
['skills', 'phno', 'name', 'email', 'course', 'branch', 'batch', 'agw']
max(d)
'skills'
min(d)
'agw'
d['paassword']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d['paassword']
KeyError: 'paassword'
dd.get('password')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dd.get('password')
NameError: name 'dd' is not defined. Did you mean: 'd'?
d.get('password')
d.setdefault('password',0)
0
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'agw': 21, 'phno': 1234566790, 'email': 'amani@gmail.com', 'password': 0}
d.setdefault('name','')
'amani'
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'agw': 21, 'phno': 1234566790, 'email': 'amani@gmail.com', 'password': 0}
len(d)
9
all(d)
True
any(d)
True
d
{'name': 'amani', 'batch': 63, 'course': 'PFS', 'branch': 64, 'skills': ['python', 'mysql', 'flask'], 'agw': 21, 'phno': 1234566790, 'email': 'amani@gmail.com', 'password': 0}
a=[1:1,2:2]
SyntaxError: invalid syntax
d = {1:1,2:2}
b=d
b[3]=3
b
{1: 1, 2: 2, 3: 3}
d
{1: 1, 2: 2, 3: 3}
c = d.copy()
c[4]=4
c
{1: 1, 2: 2, 3: 3, 4: 4}
d
{1: 1, 2: 2, 3: 3}
d = dict.fromkeys(["a","b"],0)
d
{'a': 0, 'b': 0}
d = dict.fromkeys(["c","d"[,1)
                   
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
d = dict.fromkeys(["c","d"],1)
                   
d
                   
{'c': 1, 'd': 1}
