#Task-2 Employee Data
import re
def validate_employeee(emp_id,email):
    emp_id_patt=r'^EMP-\d{4}$'
    email_patt=r'^[a-zA-z0-9._%+-]+@company\.com$'
    if not re.fullmatch(emp_id_patt,emp_id):
        raise ValueError("Employee ID Format is Invalid format-EMP-2004")
    if not re.fullmatch(email_patt,email):
        raise ValueError("Email format must be name@company.com")
    return True