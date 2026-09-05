'''
fa = eval(input("Follow Account:"))
cf = eval(input("Close Friend Accout:"))

if fa:
  if cf:
    print("Story is visible")
  else:
    print("Not in Close Friend List")
else:
  print("Follow the Account First")
  ''' 

'''
rs = eval(input("Registration Status:"))


if rs:
  ef = eval(input("Entry Fee Paid:"))
  if ef:
    print("Tournament Entry Confirmed")
  else:
    print("Entry fee not paid")
else:
  print("Register for the Tournament")
'''

file = eval(input("File Status:"))
per = eval(input("Permission"))

if file:
  if per:
    print("File Opened Successfully")
  else:
    print("permission denied")
else:
  print("No access")