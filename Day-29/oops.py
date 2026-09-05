class Flipkart:
  products = {'shirts':1000,'handbag':2000,'pants':3000}  #class attributes
  discount = 30

  @classmethod     #class method
  def display(cls):
    print(cls.products)

  def userinfo(self,name,phone,address):   #instance method
    self.name = name         #instance attributes
    self.phone = phone
    self.address = address
    print(f"Hello {self.name}, Welcome to the flipkart")

  @staticmethod   #static method
  def displaydiscount():
    print(f"{Flipkart.discount}% discount is going on,grab the products")

amani = Flipkart()
#obj->methods
amani.userinfo('amani',9856742298,'Hyd')
amani.display()
amani.displaydiscount()

#using obj we can access inst,cls,static methods and cls,inst attributes
#using class name we can access cls,static methods and cls attributes
#obj->var
print(amani.products)
print(amani.name)
#class->method,var
Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)

