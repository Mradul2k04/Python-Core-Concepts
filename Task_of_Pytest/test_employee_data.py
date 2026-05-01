import pytest 
from employee_data import validate_employeee
def test_vaild_employeeID_and_email():
    assert validate_employeee("EMP-1555","mradul155@company.com")
    
def teat_invalid_EmployeeID():
    with pytest.raises(ValueError,match="Employee ID Format is Invalid format-EMP-2004"):
        validate_employeee("EMP-12","mradul155@company.com")

def test_invalid_Email():
    with pytest.raises(ValueError,match="Email format must be name@company.com"):
        validate_employeee("EMP-1234","mradul.sharma_cs.aiml@gla.ac.in")