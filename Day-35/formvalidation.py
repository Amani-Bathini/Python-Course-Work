import re
'''
#Full name validation
fullname = input("Enter your full name:")
pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=re.fullmatch(pattern,fullname)
print("Valid full name" if res else "Invalid full name")
'''
'''
---------------------Email Validation---------------------------
email = input("Enter your email:")
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res=re.fullmatch(pattern,email)
print("Valid email" if res else "Invalid email")
'''
'''
-----------------Mobile Number Validation------------------------
mobile = input("Enter your mobile number:")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
res = re.fullmatch(pattern,mobile)
print("Valid mobile number" if res else "Invalid mobile number")
'''
'''
------------------password Validation-----------------------------
password = input("Enter your password:")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res=re.fullmatch(pattern,password)
print("Valid password " if res else "Invalid password")
'''
'''
------------------------user Validation-----------------------------
username = input("Enter your username:")
pattern = r'^[a-zA-Z0-9._]{5,20}$'
res = re.fullmatch(pattern,username)
print("Valid username" if res else "Invalid username")
'''
'''
------------------------PAN Validation------------------------------
pan = input("Enter your PAN number:")
pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
res = re.fullmatch(pattern,pan)
print("Valid PAN number" if res else "Invalid PAN number")
'''

#---------------------------Aadhar Validation---------------------------
aadhar = input("Enter your Aadhar number:")
pattern = r'^\d{4}\s\d{4}\s\d{4}$'
res = re.fullmatch(pattern,aadhar)
print("Valid Aadhar number" if res else "Invalid Aadhar number")