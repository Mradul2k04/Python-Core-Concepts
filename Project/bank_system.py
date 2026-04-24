class Account:
    def __init__(self,balance,account_holder):
        self.__balance=balance
        self.__account_holder=account_holder
    @property
    def account_balance(self):
        return self.__balance
    def _update_balance(self,new_balance):
        self.__balance=new_balance
        
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposit : {amount} \nNew Balance : {self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance -=amount
            return True
        else:
            print("Insufficient Funds")
            return False
class SavingAccount(Account):
    def __init__(self, balance, account_holder,interest_rate):
        super().__init__(balance,account_holder)
        self.interest_rate=interest_rate
    def withdraw(self,amount):
        if (self.account_balance-amount)>=500:
            new_bal=self.account_balance-amount
            self._update_balance(new_bal)
            print(f"Withdraw : {amount} \nBalance : {self.account_balance}")
        else:
            print("Account Reached to the Minimum balance limit")
    def add_interset(self):
        interset=(self.account_balance*self.interest_rate)/100
        self.deposit(interset)
        
class CurrentAccount(Account):
    def __init__(self,balance,account_holder,overdraft_limit):
        super().__init__(balance,account_holder)
        self.overdraft_limit=overdraft_limit
    def withdraw(self, amount):
        if amount<=(self.account_balance+self.overdraft_limit):
            new_bal=self.account_balance-amount
            self._update_balance(new_bal)
            print(f"Withdraw : {amount} \nBalance : {self.account_balance}")
        else:
            print("Denied : Overdraft Limit exceeded")  
print("---------Bank System---------")
acc=[]
obj1=SavingAccount(50000,"Mradul",5)

obj1.add_interset()
obj2=CurrentAccount(500000,"Anuj",100)

acc.append(obj1)
acc.append(obj2)
for i in acc:
    print(i.__class__.__name__)
    print(i.withdraw(1000))
    