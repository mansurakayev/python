def check(n):
    if n:
        print("YES")
    else:
        print("NO")
file = open("Test1.txt")
check(file.closed)
file.close()
check(file.closed)