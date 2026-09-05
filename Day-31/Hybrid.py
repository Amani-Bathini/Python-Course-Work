class WhatsappV1:
  def messaging(self):
    print("You can send messages")

class Whatsappv2:
  def extramessage(self):
    print("You can add emojis,stickers and gifts")

class Whatsappv3(WhatsappV1,Whatsappv2):
  def calls(self):
    print("You can make audio and video calls")

class Whatsappv4(Whatsappv3):
  def status(self):
    print("You can add the status for 24hr")

a = WhatsappV1()
a.messaging()

b = Whatsappv2()
b.extramessage()

c= Whatsappv3()
c.messaging()
c.extramessage()
c.calls()

d = Whatsappv4()
d.status()
d.messaging()
d.extramessage()
d.calls()

