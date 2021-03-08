import re
n = int(input())
for _ in range(n):
    text = input()
    print(re.search(r"^([-\+])?[0-9]*\.[0-9]+$", text) is not None)
