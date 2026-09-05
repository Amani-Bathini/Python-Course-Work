#method overloading:does not support by pyhton but indirectly we can do it by default parameters
#method overriding
#operator overloading
#->method overriding
class Hotstar:
  def __init__(self,name):
    print(f"Welcome to the Hotstar,{name}")
  def login(self):
    print("You can login to the hotstar")
  def dashboard(self):
      print("You can see the dashboard")
  def search(self):
      print("You can search")
  def playcontrollers(self):
      print("pause.resume.play")
  def history(self):
      print("You can see the recent video")
  def adds(self):
      print("Ads will run")
  def quality(self):
      print("You can have low quality")
  def downloads(self):
      print("You have no access to download")
  def access(self):
     print("You have limited access")

class PremiumHotstar(Hotstar):
   def __init__(self,name):
       print(f"Welcome to the Hotstar,{name}")
   def adds(self):
         print("Ads will not run")
   def quality(self):
         print("You can have high quality")
   def downloads(self):
         print("You have access to download")
   def access(self):
        print("You have unlimited access")

amani=Hotstar("amani")
amani.login()
amani.dashboard()
amani.search()
amani.playcontrollers()
amani.history()
amani.adds()
amani.quality()
amani.downloads()
amani.access()

anjana = PremiumHotstar("anjana")
anjana.login()
anjana.dashboard()
anjana.search()
anjana.playcontrollers()
anjana.history()
anjana.adds()
anjana.quality()
anjana.downloads()
anjana.access()




   