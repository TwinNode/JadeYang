"""
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

For each integer in nums1, check if it exists in nums2.
Do the same for each integer in nums2.
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = []
        num_i = {k for k in nums1} #no dupes
        num_j = {k for k in nums2}
        result = []
        result2 = []
        for i in num_i:
            if i not in num_j:
                result.append(i)
        output.append(result)

        for j in num_j:
            if j not in num_i:
                result2.append(j)
        output.append(result2)
        return output

#use set
class Solution:
        def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            s1, s2 = set(nums1), set(nums2) #remove dupes
            return [list(s1-s2), list(s2-s1)] #differnece of sets

#best practice
class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        ans = [[], []] # nested list

        for i in s1:
            if i not in s2:
                ans[0].append(i) # to acess nested list
        
        for i in s2:
            if i not in s1:
                ans[1].append(i)
        
        return ans
