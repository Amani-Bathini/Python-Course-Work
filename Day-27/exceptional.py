'''
try:
  #a=int(input())
  k= {1:12,12:13}
  #print(k[14])
  l=[223,456]
  #print(l[10])
  #print(10/0)
  #print('1'+1)
except ValueError:
  print("Enter Correct Datatype")
except KeyError:
  print("Key is not there")
except IndexError:
  print("Index is not there")
except ZeroDivisionError:
  print("can't divided by 0")
except TypeError:
  print("Define the Variable")
else:
  print("Error Free Program")
finally:
  print("End of the program")
'''
'''
try:
  #a=int(input())
  k= {1:12,12:13}
  #print(k[14])
  l=[223,456]
  #print(l[10])
  #print(10/0)
  print('1'+1)
except (ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
  print("Error Occured",e)
else:
  print("Error Free program")
finally:
  print("End of the program")
'''
'''
try:
  a=int(input())
  k= {1:12,12:13}
  #print(k[14])
  l=[223,456]
  #print(l[10])
  #print(10/0)
  #print('1'+1)
except Exception as e:
  print("Error Occured",e)
else:
  print("Error Free program")
finally:
  print("End of the program")
'''

try:
  amount = int(input("Enter the amount:"))
  balance = 5000
  if amount<0:
    raise Exception("Amount needs to be positive")
except Exception as e:
  print("Error Occured",e)
else:
  print("Error Free program")
finally:
  print("End of the program")
