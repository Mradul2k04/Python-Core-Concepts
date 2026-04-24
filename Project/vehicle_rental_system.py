from abc import ABC,abstractmethod
class Vehical(ABC):
    @abstractmethod
    def calculate_rent(self,days):
        pass
    def __init__(self,model,base_rent):
        self.__model=model
        self.__base_rent=base_rent
    @property
    def vehicle_model(self):
        return self.__model    
    @property
    def base_price(self):
        return self.__base_rent   
    def get_info(self):
        return f"The model name of vehicle is : {self.vehicle_model}"
class Car(Vehical):
    def __init__(self, model, base_rent,):
        super().__init__(model, base_rent)
    def calculate_rent(self,days):
        self.days=days
        rent=self.base_price*days
        print(f"The rent of car : {rent}")
class bike(Vehical):
    def __init__(self, model, base_rent):
        super().__init__(model, base_rent)
    def calculate_rent(self, days):
        self.days=days
        rent=(self.base_price*days)*0.8       

        print(f"Bike gets at 20% Dicount : {rent}")
print("-------Rental Service-------")        
Garage=[]
obj1=Car("Thar",3500)
obj2=bike("R15",500)
Garage.append(obj1)
Garage.append(obj2)
for i in Garage:
    print(i.get_info())
    i.calculate_rent(5)
        