import pytest 

from banking_sector import transfer,TransferError

def test_successful_transfer():
    assert transfer("7417407456","1511546118",500,1000)
    
def test_zero_amount():
    with pytest.raises(TransferError,match="Amount can not be 0"):
        transfer("1234567809","0123456789",0,1000)
        
def test_insufficient_balance():
    with pytest.raises(TransferError):
        transfer("123450789","1236547890",500,400)
        
def test_invalid_account_number():
    with pytest.raises(TransferError):
        transfer("61466466","1234560789",500,1000)                
            