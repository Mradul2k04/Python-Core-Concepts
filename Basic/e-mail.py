#String: "Users: mradul123, anuj45, and guest_user."
#Goal: Match a word that has letters followed by digits.

import re

String="mradul123,anuj45,guest_user"

pattern= r"[a-zA-Z]+\d+"

matches=re.findall(pattern,String)

print(matches)

