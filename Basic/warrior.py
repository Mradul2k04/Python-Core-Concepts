class warrior: #class 
    #constructor
    def __init__(self,health,power):
        self.health=health
        self.power=power
        #Methods
    def fight(self):
        return f"Wrrior attacks with {self.power} damage!"
    def alive(self):
        if self.health>0:
            return True
        else:
            return False
# Inheritance("The Parent & Child Concept")        
class SuperWarrior(warrior):
    def __init__(self,health,power):
        super().__init__(health,power)
        
    def fight(self):
        return f"Super Warrior attacks with DOUBLE power: {self.power * 2}"
    def ultimate_move(self):
        return "Super Warrior uses Ultimate Attack"
#Object Declaration                
obj=warrior(2,100)
obj2= SuperWarrior(50,200)
print(obj2.ultimate_move())

print(obj2.fight())
print(f"Is the warrior alive ?{obj.alive()}")                