class WhatsappV1:
  def status(self):
    print("You can add images and videos")

class Whatsappv2(WhatsappV1):
  def status(self):
    super().status()
    print("You can add music and stickers")

class Whatsappv3(Whatsappv2):
  def status(self):
    super().status()
    print("You can like and you can add reaction")

c= Whatsappv3()
c.status()
