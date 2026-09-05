class Instagram:
  def __init__(self,username,password):
    self.username = username
    self.__password = password
    self._posts = []

  #to access private attribute we need to declare a method
  def getpassword(self):
    return self.__password
  #to update
  def setpassword(self,newpassword):
    self.__password = newpassword
  
  #to access protected attribute we need to declare a property
  @property
  def accesspost(self):
    return self._posts
  #to update
  @accesspost.setter
  def accesspost(self,newpost):
    self._posts.append(newpost)

  def display(self):
    print(self.username,self.__password,self._posts)

amani = Instagram('amani','amani@123')
amani.display()
print(amani.username) #public
print(amani.getpassword())#private
print(amani.accesspost)#protected

#updating
amani.username = "akhila"
print(amani.username)
amani.setpassword("akhila@123")
print(amani.getpassword())
amani.accesspost = "sunrise.png"
amani.accesspost = "beach.png"
amani.accesspost = "sunset.png"
print(amani.accesspost)
