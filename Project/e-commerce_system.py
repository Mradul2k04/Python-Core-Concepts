class Product:
    def __init__(self,name,price):
        self.__name = name
        self.__price=price
    @property
    def total_price(self):
        return self.__price 
    @property
    def product_name(self):
        return self.__name 
    
    def get_details(self):
        return f"The Product price : {self.__price}and The Product name :  {self.__name}"
class Electronic(Product):
    def __init__(self,name,price,warranty):
        super().__init__(name,price)
        self.warranty=warranty
      
    def get_details(self):
        return f"The Product price : {self.total_price} \nThe Product name : {self.product_name} \nThe warranty of product is : {self.warranty}"
    
class Clothing(Product):
    def __init__(self, name, price,size):
        super().__init__(name,price)
        self.size=size   
    def get_details(self):
        return f"The Product price : {self.total_price}\nThe Product name is : {self.product_name} \nThe size  of cloth is : {self.size}"   
items = []
obj1=Electronic("kettle",1000,24)
obj2=Clothing("T-shirt",500,"XL")
items.append(obj1)
items.append(obj2)
print("----Welcome to E-commerce System----\n")
for i in items:
    print(i.__class__.__name__)
    print(i.get_details())
