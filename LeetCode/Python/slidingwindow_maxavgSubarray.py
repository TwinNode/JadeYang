class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
  
        currentsum = maxsum = sum(nums[:k])

        for i in range(k,len(nums)):
            currentsum += nums[i] - nums[i-k]
            maxsum = max(maxsum,currentsum)
            
        return maxsum/k
