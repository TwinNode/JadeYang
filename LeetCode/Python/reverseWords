"""
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"

Input: s = "a good   example"
Output: "example good a"
"""
#Basic - use list comprehension
class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()
        return ' '.join([x for x in text[::-1]])
                         
#Improved - no need to use list comprehension
class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()
        return ' '.join(text[::-1])
