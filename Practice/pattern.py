import re
text = "The records show that AL-9582, BK-1024, and CM-8832 are processed. Error found in id Z-99."
pattern=r'[A-Z]{2}-\d{4}'
print(re.findall(pattern,text))