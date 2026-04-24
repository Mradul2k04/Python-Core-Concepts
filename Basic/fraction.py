class Fraction:
    def __init__(self,x,y):
        self.num=x
        self.don=y
        
    def __str__(self):
        return '{}/{}'.format(self.num,self.don)
    
    
    def __add__(self, other):
        new_num=self.num*other.don+other.num*self.don
        new_don=self.don*other.don
        return '{}/{}'.format(new_num,new_don)  
    
    def __sub__(self, other):
        new_num=self.num*other.don-other.num*self.don
        new_don=self.don*other.don
        return '{}/{}'.format(new_num,new_don)  
          
fr1=Fraction(3,4)
fr2=Fraction(1,2)    
print(fr1-fr2)   
        
        