import re
class TransferError(Exception):
    pass

def transfer(from_account,to_account,amount,balance):
    acc_patt=r"^\d{10}$"
    
    if not re.match(acc_patt,from_account) or not re.match(acc_patt,to_account):
        raise TransferError("Invalid account Number. Account must be 10 digit")
    
    elif not amount>0:
        raise TransferError("Amount can not be 0")
    elif amount>balance:
        raise TransferError("Insufficient balance for this transfer")
    
    return True
    
        
        