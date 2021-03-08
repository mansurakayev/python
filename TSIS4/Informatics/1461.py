b = list(map(int, input().split()))
ans,count,i=0,0,0
cnt = 1
while i < len(b):
    if i + 1 < len(b) and b[i] == b[i+1]:
        cnt += 1
        i += 1
        continue
    if cnt >= 3:
        ans += cnt
        del b[i-cnt+1:i+1]
        cnt=0
        i = 0
    else:
        cnt = 1
        i += 1
#print(*b)
print(ans)
#print(len([i for i in b if i == -1]))
#0 1 2 3 4 5
#1 1 1 4 5 6