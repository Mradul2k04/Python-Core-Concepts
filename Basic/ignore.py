import re

pattern=r"Python"

data="python is very powerful language and python have lots of methods in it"

match=re.search(pattern,data,re.IGNORECASE)
print(match)

if match:
    print("found : ",match.group())
else:
    print("Not Found")