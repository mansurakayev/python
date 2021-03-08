import re
ok = False
n = int(input())
for x in range(n):
    line = input()
    if '{' in line:
        ok = True
        continue
    if '}' in line:
        ok = False
        continue
    if ok == True:
        m = re.findall(r'(#[a-fA-F0-9]{3,6})', line)
        if m:
            print(*m, sep='\n')