def IsPointInCircle(x, y, xc, yc, r):
    if ((xc - x)**2 + (yc - y)**2)**0.5 <= r: return True
    else: return False
x, y, xc, yc, r = float(input()), float(input()), float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r): print("YES")
else: print("NO")