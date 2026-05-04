#Scenario
#Create a function sanitize_input(text).[cite:16]
#Remove unwanted special characters using re.sub().[cite:16]
#Keep letters, numbers, spaces, and hyphens if needed.[cite:16]
#If cleaned text becomes empty, raise InputSanitizationError.[cite:15]

#Task
#Write one test case for input like John Doe!.[cite:16]
#Write one test case for input like !@#$%.[cite:16]
#Write one test case for input like Payment: 100$.[cite:16]
#Check cleaned output for valid text.[cite:16]
#Check exception for empty cleaned text.[cite:12][cite:18]



import re
class InputSanitizationError(Exception):
    pass

def sanitize_input(text):
    unwanted_patt=r"[^A-Za-z0-9\s-]"
    needed_text=re.sub(unwanted_patt,'',text)
    if not needed_text:
        raise InputSanitizationError("Text has been become empty after removing unwanted pattern")
    return needed_text
    
    
    
    