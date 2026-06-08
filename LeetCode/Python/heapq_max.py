from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       res = nums[:k]
       heapq.heapify(res)
 
       for num in nums[k:]:
           if num > res[0]:
              heapq.heappop(res)
              heapq.heappush(res, num)
    
       return res[0]

nums = [3,2,1,5,6,4]; k = 2
sol = Solution()
sol.findKthLargest(nums, k)