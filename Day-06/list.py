Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l =[]
l = list[]
SyntaxError: invalid syntax
l = list()
l = [1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},   None,True,False]
1
1
>>> l
[1, 12.3, (2+3j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, None, True, False]
>>> l = [1,1,1,1]
>>> l
[1, 1, 1, 1]
>>> type()l
SyntaxError: invalid syntax
>>> type(l)
<class 'list'>
>>> l = [1,2,3,4]
>>> m = [5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[-1]
4
>>> 
>>> l[1:]
[2, 3, 4]
>>> l[:2]
[1, 2]
>>> l{::-1}
SyntaxError: invalid syntax
>>> l[::-1]
[4, 3, 2, 1]
>>> 1 in l
True
>>> 2 in l
True
>>> 5 not in l
True
>>> 5 in l
False
