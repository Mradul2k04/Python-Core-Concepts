#Python use builtin package re to handel regular expression
import re

#Sample text contains two phonne number data
text="My phone number is 123-456-7890 and my home number is 987-654-3210"

#Regex pattern to match the format in text
pattern=r"\d{3}-\d{3}-\d{4}"

#match from the pattern
matches=re.findall(pattern,text)

print(matches)