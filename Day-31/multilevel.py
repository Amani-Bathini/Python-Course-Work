class WhatsappV1:
  def messaging(self):
    print("You can send messages")

class Whatsappv2(WhatsappV1):
  def calls(self):
    print("You can make audio and video calls")

class Whatsappv3(Whatsappv2):
  def status(self):
    print("You can add the status for 24hr")
a = WhatsappV1()
a.messaging()

b = Whatsappv2()
b.messaging()
b.calls()

c= Whatsappv3()
c.status()
c.calls()
c.messaging()


