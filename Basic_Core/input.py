a="Hello <<UserName>> ,How are you ?"

username =input("Enter a User Name :")
if(len(username)<3):
    print("Usename sholud be min 3 character")
else:
    a= a.replace("<<UserName>>",username)
    print(a)