class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        comp = highest = 0

        for x in gain:
            comp += x
            highest = max(highest, comp)
  
            return highest

gain = [-4,-3,-2,-1,4,3,2]
sol = Solution()
sol.largestAltitude(gain)
