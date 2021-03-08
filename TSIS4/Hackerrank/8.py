import re
pattern = r"^[879]\d{9}"
n = int(input())
for i in range(n):
    text = input()
    if re.match(pattern,text) and len(text)==10:
        print("YES")
    else:
        print("NO")