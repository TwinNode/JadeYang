"""
Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n, where n is an integer greater or equal to 1.

Your result should be within 10^-6 of the expected one.

u1 = (1 / 1!) * (1!)
u2 = (1 / 2!) * (1! + 2!)
u3 = (1 / 3!) * (1! + 2! + 3!)
...
un = (1 / n!) * (1! + 2! + 3! + ... + n!)


u3 = 1 + 1/n + 1/n(n-1)
1/((3)*0) + 1/((3)*1) + 1/((3)*(3-1))
"""

class Solution:
    def going(self, n: int)-> int:
        
        nums = 1
        total_sum = 1
        for x in range(n, 1, -1):
            nums /= x
            total_sum += nums
  
        return total_sum

#best practice
def going(n):  
    s = 1.0
    for i in range(2, n + 1):
        s = s/i + 1
    return int(s * 1e6) / 1e6
  # e.g. s = 0.12345678, s*1e6 = 123456.78, int(s*1e6) =123456, /1e6 = 0.123456
