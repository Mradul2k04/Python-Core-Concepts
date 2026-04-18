#Serialization is the process of Converting the python data type to JSON format .
#DeSerialization is the opposite to Serialization


#Serialization using Json using List 
import json

L=[1,2,3,4]
with open("File_Handling/Demo.json","w") as f:
    json.dump(L,f)
    
#Dict
d={
    'name':'mradul',
    'age':33,
    'gender':'male'
}
with open("File_Handling/demo.json",'w') as f:
    json.dump(d,f,indent=4) #indent give the space 


#DeSerialization
import json
with open("File_Handling/demo.json","r") as f:
    d=json.load(f)
    print(d)
    print(type(d))
    
    
# Serialization and DeSerialization in Tuple
    
import json

t=(1,2,3,4)

with open("File_Handling/demo.json","w") as f:
    json.dump(t,f)    #If we Serialization using Tuple it give us List only same as in DeSerialization
    
    
#Program in Dict
class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
        
        
        
person=Person('Mradul','Sharma',20,'male')

#Serialization 
import json

def show_object(person):
    if isinstance(person,Person):
        return{'name':person.fname+' '+person.lname,'age':person.age,'gender':person.gender}
    

with open("File_Handling/demo.json","w") as f:
    json.dump(person,f,default=show_object,indent=4)
    
#Deserialization
import json
with open("File_Handling/demo.json","r") as f:
    d=json.load(f)
    print(d)
    print(type(d))
    
    
    
    
    
    
