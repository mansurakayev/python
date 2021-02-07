def IsPointInSquare(x, y):
    if (x >= 0 and y >= 0) and (x + y <= 1): return True
    elif (x >= 0 and y <= 0) and (x - y <= 1): return True
    elif (x <= 0 and y >= 0) and (y - x <= 1): return True
    elif (x <= 0 and y <= 0) and (x + y >= -1): return True
    return False
x, y = float(input()), float(input())
if IsPointInSquare(x, y): print("YES")
else: print("NO")