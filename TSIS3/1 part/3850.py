a = list(map(int,input().strip().split()))
print(*([i for i in a if i] +[0]*a.count(0)))