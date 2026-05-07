class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = finder = 0

        for num in nums:
            if num != 0: #when not 0, swap two numbers
                nums[index], nums[finder] = nums[finder], nums[index]
                index += 1
            finder +=1   
