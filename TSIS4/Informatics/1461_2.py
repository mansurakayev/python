mylist, cnt, ans, i = list(map(int, input().split())), 1, 0, 0
while i < len(mylist):
    if i + 1 < len(mylist) and mylist[i] == mylist[i+1]:
        cnt += 1
        i += 1
        continue
    if cnt >= 3:
        ans += cnt
        ind = i
        while cnt > 0:
            del mylist[ind]
            ind -= 1
            cnt -= 1
        i = 0
    else:
        cnt = 1
        i += 1
print(ans)