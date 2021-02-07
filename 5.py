class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x, sum_d, pro_d = str(n), 0, 1
        for i in x:
            sum_d += int(i)
            pro_d *= int(i)
        return pro_d - sum_d