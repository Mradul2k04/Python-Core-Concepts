import re

text=["data.txt","image.jpg","data2.csv","dat_final.txt"]

pattern= r"^data.*\.txt$"

for i in text:
    if re.search(pattern,i):
        print(f"Match found {i}")
