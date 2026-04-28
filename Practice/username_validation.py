import re
username=["@user123", "user123", "@abc", "@USER123", "@pythonprog"]

pattern=r'@[a-z0-9]{5,10}'
for i in username:
    if re.fullmatch(pattern,i):
        print(f"Valid :{i}")
    else:
        print(f"Invalid: {i} ")