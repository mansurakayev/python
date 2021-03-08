import re
n = int(input())
for _ in range(n):
    text = input().strip()
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", text) and not re.search(r"([\d])\1\1\1", text.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")