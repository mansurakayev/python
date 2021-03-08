import re
n = int(input())
for i in range(0,n):
    text = input()
    text = re.sub(r"\ \&\&\ "," and ",text)
    text = re.sub(r"\ \|\|\ "," or ",text)
    text = re.sub(r"\ \&\&\ "," and ",text)
    text = re.sub(r"\ \|\|\ "," or ",text)
    print(text)