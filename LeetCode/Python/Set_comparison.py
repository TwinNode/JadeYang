from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        char1=Counter(word1)
        char2=Counter(word2)

        if len(word1) != len(word2):
            return False
        
        char1=Counter(word1)
        char2=Counter(word2)
        
        samecharacters = set(word1) == set(word2)
        samefreq = sorted(char1.values()) == sorted(char2.values())

        return samecharacters and samefreq

  """
  Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""
