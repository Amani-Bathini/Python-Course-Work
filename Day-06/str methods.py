Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c = 'strings.py'
>>> c.startswith('str')
True
>>> c.endswith('python')
False
>>> c.endswith('py')
True
>>> c.islower()
True
>>> c.isupper()
False
>>> 'Pythonvr13'.isupper()
False
>>> 'PYHTONVR13'.isupper()
True
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> ;        ;.isspace()
SyntaxError: invalid syntax
>>> '              '.isspace()
True
>>> 'b         '.isspace()
False
>>> 'my@var@'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> 'This is title'.istitle()
False
>>> ;This Is Title'.istitle()
SyntaxError: unterminated string literal (detected at line 1)
>>> 'This Is Title'.istitle()
True
