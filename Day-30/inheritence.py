class WhatsappV1:
  def __init__(self,name):
    self.name = name
    print(f"Welcome to the whatsapp-v1 {self.name}!")
  def messaging(self):
    print("You can send messages")

class Whatsappv2(WhatsappV1):
  def __init__(self,name):
      self.name = name
      print(f"Welcome to the whatsapp-v2 {self.name}!")
  def calls(self):
    print("You can make audio and video calls")

amani = WhatsappV1('amani')
amani.messaging()
akhila = Whatsappv2("akhila")
akhila.messaging()
akhila.calls()

