import pytest 
from task_5 import sanitize_input ,InputSanitizationError

def test_valid_input():
    assert sanitize_input("John Doe!")=="John Doe"
    
def test_invalid_input():
    with pytest.raises(InputSanitizationError,match="Text has been become empty after removing unwanted pattern"):
        sanitize_input("!@#$%")
        
def test_text_invalid_input():
    assert sanitize_input("Payment : 100$")=="Payment  100"
            