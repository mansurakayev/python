import re
n = int(input())
for _ in range(n):
    text = ''.join(sorted(input()))
    a = re.search(r'[A-Z]{2}', text)
    b = re.search(r'\d\d\d', text)
    c = re.search(r'[^a-zA-Z0-9]', text)
    d = re.search(r'(.)\1', text)
    if a and b and not c and not d and len(text) == 10:
        print('Valid')
    else:
        print('Valid')