class WhatsappV1:
  def messaging(self):
    print("You can send messages")

class Whatsappv2:
  def calls(self):
    print("You can make audio and video calls")

class Whatsappv3(WhatsappV1,Whatsappv2):
  def status(self):
    print("You can add the status for 24hr")
a = WhatsappV1()
a.messaging()

b = Whatsappv2()
b.calls()

c= Whatsappv3()
c.status()
c.calls()
c.messaging()


