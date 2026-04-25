from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def __init__(self,battery_level):
        self.check_level=battery_level
        
    @abstractmethod
    def operate(self):
        pass
    
    @property
    def check_level(self):
        return self.__battery_level
    
    @check_level.setter
    def check_level(self,values):
        if values>100:
            self.__battery_level=100
            print("Capping battey at 100%")
        elif values <0:
            self.__battery_level=0
            print("Battery cannot be negative set as 0")
        else:
            self.__battery_level=values          
            
class SmartLight(SmartDevice):
    def __init__(self, battery_level,color):
        super().__init__(battery_level)
        self.color=color
        
    def operate(self):
        print(f"Lighting up the room in {self.color}! Battery at {self.check_level} ") 
        
class SmartSpeaker(SmartDevice):
    def __init__(self, battery_level,volume):
        super().__init__(battery_level)
        self.volume=volume
        
    def operate(self):
        print(f"Playing Music at {self.volume}! Battery at {self.check_level}")   

print("---------Smart Home System---------")
Device=[]
obj1=SmartLight(80,"Red")
obj2=SmartSpeaker(-5,200)    
Device.append(obj1)
Device.append(obj2)
for i in Device:
    i.operate()
    