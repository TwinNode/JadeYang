"""
Input: s = "leet**cod*e"
Output: "lecoe"
"""

#reversed order
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        k = len(s)-1
        star = 0

        while k >= 0:
            if s[k] == "*":
                star += 1
            else:
                if star > 0:
                    star -= 1
                else:
                    ans.append(s[k]) 
            k -= 1    

        return "".join(ans[::-1])


class Solution:
    def removeStars(self, s):
        stack = []
        for char in s:
            if char == "*" :
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)

s = "leet**cod*e" #"lecoe"
sol = Solution()
sol.removeStars(s)
