# condition for password : Password contains at least one digit or at least one uppercase letter

import re
password=input("Enter password")

pattern=r'[0-9A-Z]'

if re.findall(pattern,password):
    print("Valid Password")
else:
    print("Invalid Password")