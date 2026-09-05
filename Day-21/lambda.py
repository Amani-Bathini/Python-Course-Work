'''
#finding greatest number using lambda
greater = lambda a,b: a if a>b else b
print(greater(12,13))
print(greater(20,14))
print(greater(50,75))
print(greater(35,20))
'''

'''
wish = lambda name: f'Welcome to the course {name}'
print(wish("Amani"))
print(wish("Anjana"))
print(wish("Akhila"))
'''

'''
#finding even or odd
iseven = lambda n : "Even" if n%2 == 0 else "Odd"
print(iseven(34))
print(iseven(23))
print(iseven(74))
print(iseven(87))
'''

'''
#finding avg of the numbers
avg = lambda a,b,c: (a+b+c)/3
print(avg(4,5,6))
print(avg(30,45,20))
'''

'''
#to extract the domain from the mail
domain = lambda mail: (mail.split('@')[-1]).split('.')[0]
print(domain('amani@gmail.com'))
print(domain('amani@codegnan.com'))
print(domain('amani@outlook.com'))
print(domain('amani@yahoo.com'))
'''

'''
#calculating prices with 18% GST
gst = lambda price:price + price*0.18

print(gst(1000))
print(gst(5000))
print(gst(8000))  
'''

'''
#Calculate Prices with 18% GST Using Lambda and Map
prices = [5678,8765,5467,1123,1600,3000]
res = list(map(lambda price : price +price*0.18,prices))
print(res)
'''

'''
names = ['akhila','amani','anjana','reena']
res = list(map(lambda name: name.title(),names))
print(res)
'''

'''
prices = [1400,1600,1800,1900,15000]
dis = list(map(lambda price:price-price*0.3,prices))
print(dis)
'''

'''
prices = [1400,1600,16000,1800,1900,15000,20000]
dis = list(filter(lambda price:price>5000,prices))
print(dis)
'''

'''
names = {'amani','anjana','akhila','reena'}
res = list(filter(lambda name:len(name)>5,names))
print(res)
'''

'''
from functools import reduce
l = [3,567,6,24,124,435,462]
res = reduce(lambda sum,i:sum+i,l)
print(res)
'''

'''
from functools import reduce
names =['amani','anjana','akhila','reena']
res = reduce(lambda res,i:res+' '+i,names)
print(res)
'''

products={'sugar':60,'salt':50,'eggs':90,'cooking oil':120,'bread':45}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))