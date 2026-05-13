class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_len = zeros = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while (zeros > k):
                if (nums[left] == 0):
                    zeros -= 1
                left += 1

            current_len = right-left+1
            max_len = max(max_len, current_len)

        return max_len

  """
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
