class Atm:
    #constructor
    def __init__(self):
        self.pin=" "
        self.balance=0
        self.menu()
    def menu(self):
        user_input = input("""
        Hello how can I help you?      
        1. Press 1 to create Pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit 
              """)  
        
        if user_input =='1':
            #create pin
            self.create_pin()
            
        elif user_input =='2':
            #change pin
            self.change_pin()
        elif user_input =='3':
            #check balance
            self.check_balance()
        elif user_input =='4':
            #withdraw
            self.withdraw_money()
        else:
            exit()
     
    def create_pin(self):
        user_pin=input("Enter your Pin : ") 
        self.pin=user_pin
        
        user_balance=int(input("Enter your Balance : "))
        self.balance=user_balance
        
        print("Pin created Succesfully")
        self.menu()
      
    def change_pin(self):
        old_pin=input("Enter old pin : ")    
        
        if old_pin==self.pin:
            new_pin=input("Enter the pin : ")
            self.pin=new_pin
            print("Pin change succesfull")
            self.menu()
        else:
            print("Wrong Pin Inserted ") 
        self.menu()      
        
    def check_balance(self):
        user_pin = input("Enter your Pin : ")
        if user_pin==self.pin:
            print("Your Balance is :",self.balance)
            self.menu()
        else:
            print("Pin not matched")   
            self.menu() 
            
    def withdraw_money(self):
        user_pin=input("Enter your pin : ")
        withdraw_amount=int(input("Enter amount you have to withdraw : "))
        if user_pin==self.pin:
            if withdraw_amount<=self.balance:
                self.balance=self.balance-withdraw_amount
                print("Amount Withdraw Succesfull",self.balance )
            else:
                print("Balance is Low")    
                self.menu()
        else:
            print("Incorrect Pin") 
            self.menu() 
        
obj=Atm()
print(type(obj)) 
       
    