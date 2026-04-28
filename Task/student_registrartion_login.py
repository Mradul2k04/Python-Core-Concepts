#Student Login and Registration Regex 
#Part 1: Registration
#Write a program that takes the following input from the user:
#Student name
#Student address
#Student ID
#Password
#The program must validate each field using regex before registration is successful.
#Registration rules
#Student name: Must contain only letters and spaces, and length should be 3 to 30 characters.
#Address: Must contain letters, numbers, spaces, commas, periods, hyphens, and slashes, and length should be 10 to 100 characters.
#Student ID: Must start with STU followed by exactly 4 digits, for example STU1024.
#Password: Must be 8 to 16 characters long and contain at least one uppercase letter, one lowercase letter, one digit, one special character, and no spaces.

#Part 2: Login
#After successful registration, ask the user to enter:
#Student ID
#Password
#The login should be successful only if:
#The entered student ID matches the registered student ID.
#The entered password matches the registered password.
#If both match, print:
#Login successful
#Otherwise, print:
#Invalid student ID or password


import re
import json
import os
Data_file="registrartion_data.json"

def Registration():
    print("------------Registration Page----------")
    stu_name=input("Enter your Name :")
    stu_address=input("Enter your Address :")
    stu_id=input("Enter your ID :")
    password=input("Enter your password :")

    stu_name_patt=r'^[A-Za-z\s]{3,30}$'
    stu_address_patt=r'^[A-Za-z0-9\s,.\-/]{10,100}$'
    stu_id_patt=r'^STU\d{4}$'
    password_patt=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@$%&*])[^\s]{8,16}$'
    
    if not re.fullmatch(stu_name_patt,stu_name):
        print ("Error :Name must be letters/spaces (3-30 chars) " )
        
    elif not re.fullmatch(stu_address_patt,stu_address):
        print ("Error: Address is too short or contains invalid characters.")
        
    elif not re.fullmatch(stu_id_patt,stu_id):
        print ("Error: ID must start with STU followed by 4 digits.")
        
    elif not re.fullmatch(password_patt,password):
        print ("Error: Password must have 1 Upper, 1 Lower, 1 Digit, 1 Special (8-16 chars).")
    else:
        print("Registration Successful ")
        stu_details={"Name":stu_name,
                     "id":stu_id,
                     "Adderss":stu_address,
                     "password":password}
        with open("Task\Data_file","w") as f:
            json.dump(stu_details,f)
            return stu_id,password
        
#Login

def Login(reg_id,reg_pass):
    print("----------Login Page----------")
    stu_id=input("Enter Login ID :")
    stu_pass=input("Enter you password :")
    
    if stu_id==reg_id and stu_pass==reg_pass:
        print("Login Successful !")
    else:
        print("Invalid ID or password")
        return Login(reg_id,reg_pass)
    
    
def Main():
    print("\n1.Registration New Account")
    print("2 Login to Your Account")
    choice=input("Select Option (1 or 2)")
    
    if choice=="1":
        reg_id,reg_pass=Registration()
        Login(reg_id,reg_pass)
    elif choice =="2":
        if os.path.exists("Task\Data_file"):
            with open("Task\Data_file","r") as f:
                stored_details=json.load(f)
                Login(stored_details["id"],stored_details["password"])
                print("Welcome Back !")
        else:
            print("No data found")
            Main()
    else:
        print("Invalid Choice ")
        Main()
Main()        