import re

'''
pattern = r'[0-9]'
text = 'codegnan'
res = re.match(pattern,text)  #checks whether the text starts with the given pattern
print(res.group() if res else "Pattern Not Found")
'''
'''
pattern = r'2'
text = 'codegnan2026'
res = re.search(pattern,text)  #checks whether the text present in the  given pattern(checks entire text)
print(res.group() if res else "Pattern Not Found")
'''
'''
pattern = r'[0-9]'
text = 'codegnan2026 python version 3.14'
res = re.findall(pattern,text)  #Returns all matching values as a list.
print(res)
'''
'''
pattern = r'[0-9]'
text = 'codegnan2026 python version 3.14'
res = re.finditer(pattern,text) #returns matched strings with indexes
for i in res:
  print(i.group(),i.start())
'''
'''
#validation
pattern = r'[0-9]{2}'
text = '12'
res = re.fullmatch(pattern,text) #Checks whether the entire string matches the pattern.
print(res.group() if res else "Pattern Not Found")
'''
'''
pattern = r'[,(#]'
text = 'python,java(html#css'
res = re.split(pattern,text)  #Splits a string using a Regex pattern.
print(res)
'''
'''
pattern = r'[0-9]'
text = 'python version 3.14,batch-63'
res = re.sub(pattern,'*',text)  #Used to replace matching text.
print(res)
'''
'''
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect Egfhjet hgjeokj'
res = re.findall(pattern,text)  
print(res)
'''
'''
pattern = r'^(91)'
text = '9123456789'
res = re.findall(pattern,text)  
print(res)
'''
'''
pattern = r'0$'
text = '91234567890'
res = re.findall(pattern,text)  
print(res)
'''
'''
pattern = r'to*' #0 or more occurances
text = 't to too tooo tooooo tdfghi'
res = re.findall(pattern,text)  
print(res)

pattern = r'to*' #1 or more occurances
text = 't to too tooo tooooo tdfghi'
res = re.findall(pattern,text)  
print(res)

pattern = r'([a-zA-Z])*' #0 or more occurances
text = 'Codegnan Programming'
res = re.findall(pattern,text)  
print(res)

pattern = r'91|0'
text = '05678'
res = re.findall(pattern,text)  
print(res)
'''
'''
pattern = r'[aeiouAEIOU]'
text = 'codegnan programming'
res = re.findall(pattern,text)  
print(res)
'''
