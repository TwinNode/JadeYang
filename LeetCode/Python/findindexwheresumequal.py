class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = x = 0

        while x < len(nums):
            rightsum = total-leftsum-nums[x]
            if (leftsum == rightsum):
                return x
            else:   
                leftsum += nums[x]
                x+=1
        
        return -1
    
class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        leftsum = 0
        for x, num in enumerate(nums):
            rightsum = total - leftsum - num
            if leftsum == rightsum:
                return x
            leftsum += num

        return -1     
