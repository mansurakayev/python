def IsPointInSquare(x, y):
    if -1 <= x <= 1 and -1 <= y <= 1: return True
    else: return False
x, y = float(input()), float(input())
if IsPointInSquare(x, y): print("YES")
else: print("NO")