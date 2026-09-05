data = {
  123456: {'pin':1234,'balance':7000,'history':[]},
  234561: {'pin':1234,'balance':5000,'history':[]},
  345612: {'pin':1234,'balance':6000,'history':[]},
  456123: {'pin':1234,'balance':9000,'history':[]}
}

def menu():
  print('[C]heck Balance')
  print('[D]eposit')
  print('[W]ithdraw')
  print('[P]Change Pin')
  print('[V]iew Transactions')
  print('[E]xit')

def login():
  global acc_num
  acc_num = int(input("Enter account number:"))
  pin = int(input("Enter pin:"))
  if acc_num in data and data[acc_num]['pin'] == pin:
    print("Login Successful")
    return True
  else:
    print("Invalid Login")
    return False
  
def checkbalance():
    print("Current Balance:",data[acc_num]['balance'])

def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance'] += amount
    print(f'{amount} is successfully deposited')
    data[acc_num]['history'].append(f'{amount} is deposited+++++++')

def withdraw():
    amount = int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        print(f'{amount} is successfully withdraw')
        data[acc_num]['history'].append(f'{amount} is withdraw-------')
    else:
        print("Insufficent Balance")

def changepin():
    old_pin = int(input("Enter your current PIN: "))

    if data[acc_num]['pin'] == old_pin:
        new_pin = int(input("Enter your new PIN: "))
        confirm_pin = int(input("Confirm your new PIN: "))

        if new_pin == confirm_pin:
            data[acc_num]['pin'] = new_pin
            print("PIN changed successfully")
        else:
            print("New PIN and confirm PIN do not match")
    else:
        print("Incorrect current PIN")


def viewtransactions():
    if data[acc_num]['history']:
        print("--------------Transactional History-----------")
        for i in data[acc_num]['history']:
            print(i)
    else:
        print("No Trasaction History")

