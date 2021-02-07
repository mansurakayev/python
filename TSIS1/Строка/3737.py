s, g = input(), 0
if len(s) % 2 == 0: g = int(len(s) / 2)
else: g = int(len(s) /2 + 1)
print(s[g:] + s[:g])