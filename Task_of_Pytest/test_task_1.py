
import pytest 
from task_1 import calculate_total

def test_valid_items_price_and_valid_tax_rate():
    assert calculate_total([100,200,300],0.8) == 604.8
    
def test_for_negative_price():
    with pytest.raises(ValueError ,match="Items price can not be negative"):
     calculate_total([-100,200-500],0.5)    
    
def test_for_invalid_tax_rate():
    with pytest.raises(ValueError,match="Tax rate must be in range"):
         calculate_total([100,500,600],2)