class SecurityError(Exception):
    def __init__(self,message):
        print(message)
        
    def logout(self):
        print("logout")    


class Google:
    def __init__(self,name,email,password,device):
        self.name=name
        self.email=email
        self.password=password
        self.device=device
        
    def login(self,email,password,device):
            if device !=self.device:
                raise SecurityError("Login Security Breach")
            if email ==self.email and password==self.password:
                print("Welcome")
            else:
                print("login error")
obj =Google("mradul","mradul.45465@gamil.com","45114161","android")
try:
    obj.login("mradul.45465@gamil.com","45114161","android") 
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print("database connection closed")                           
                      
            