#super is always pointing to the single parent ,so if multiple parents are there we use class methods
class WhatsappV1:
  def status(self):
    print("You can add images and videos")

class Whatsappv2(WhatsappV1):
  def status(self):
    print("You can add music and stickers")

class Whatsappv3(WhatsappV1,Whatsappv2):
  def status(self):
    WhatsappV1.status(self)
    Whatsappv2.status(self)
    print("You can like and you can add reaction")

c= Whatsappv3()
c.status()
