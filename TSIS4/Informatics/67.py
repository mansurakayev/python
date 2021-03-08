a = int(input())
b = list(map(int, input().split()))
if len([b[i] for i in range(1, len(b)) if (b[i] > 0 and b[i - 1] > 0) or (b[i] < 0 and b[i - 1] < 0)]) > 0:
    print("YES")
else:
    print("NO")
