import re
pattern=r"([a-zA-Z0-9])\1+"
text = input()
m=re.search(pattern,text)
if m:
    print (m.group(1))
else:
    print (-1)    