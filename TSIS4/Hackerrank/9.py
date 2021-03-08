import re
n = int(input())
for i in range(n):
    name, text = input().split()
    mailpattern=r"<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,4}>"
    if re.match(mailpattern,text):
        print(name,text)