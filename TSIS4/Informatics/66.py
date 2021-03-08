a = int(input())
b = list(map(int, input().split()))
print(len([b[i] for i in range(1, len(b)) if b[i] > b[i - 1]]))
