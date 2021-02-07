n, k = int(input()), 0
while True:
    if n <= 2**k:
        print(k)
        break
    k += 1