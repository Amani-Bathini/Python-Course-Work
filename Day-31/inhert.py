class WhatsappV1:
  def messaging(self):
    print("You can send messages")

class Whatsappv2(WhatsappV1):
  def calls(self):
    print("You can make audio and video calls")

a = WhatsappV1()
a.messaging()

b = Whatsappv2()
b.messaging()
b.calls()


