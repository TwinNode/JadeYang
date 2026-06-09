from typing import List
from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        res = []

        # answer ---------------------------------
        for spell in spells:
            right = len(potions) -1
            left = 0
            while left <= right:
                mid = (left + right) // 2

                if spell * potions[mid] >= success:
                    right = mid -1
                else:
                    left = mid +1

            res.append(len(potions) - left)

        # best practice --------------------------
            count = len(potions) - bisect_left(potions, (success + spell -1) // spell)
            # to round up: (dividend + divisor -1) // divisor
            res.append(count)

        return res


spells = [5,1,3];potions = [1,2,3,4,5];success = 7
#Output: [4,0,3]
sol = Solution()
sol.successfulPairs(spells,potions,success)