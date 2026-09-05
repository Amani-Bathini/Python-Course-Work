from abc import ABC,abstractmethod
class Phonepay:
  def senderinfo(self):
    print("You can enter their mobile number or scan")
  def amount(self):
    print("You can enter amount")
  def pin(self):
    print("You need to enter the pin")

  @abstractmethod
  def transaction(self):
    pass

class HDFC(Phonepay):
  def transaction(self):
    print("Payment using HDFC Bank")

class SBI(Phonepay):
  def transaction(self):
      print("Payment using SBI Bank")
  
class AXIS(Phonepay):
  def transaction(self):
      print("Payment using AXIS Bank")

class UNION(Phonepay):
  def transaction(self):
      print("Payment using UNION Bank")
  

class ICIC(Phonepay):
 def transaction(self):
     print("Payment using ICIC Bank")

amani = HDFC()
amani.senderinfo()
amani.amount()
amani.pin()
amani.transaction()
anjana = SBI()
anjana.amount()
anjana.pin()
anjana.transaction()
reena = AXIS()
reena.amount()
reena.pin()
reena.transaction()
akhila = UNION()
akhila.amount()
akhila.pin()
akhila.transaction()
abhi = ICIC()
abhi.amount()
abhi.pin()
abhi.transaction()
