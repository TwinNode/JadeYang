class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ('aeiou')
       
        vowel_count = current_count = len([char for char in s[:k] if char in vowel]) 
        #starting point : how many vowels within the windown at start
        
        for i in range(k, len(s)):
            if (s[i] in vowel):
                current_count += 1
            if (s[i-k] in vowel):
                current_count -= 1
            vowel_count = max(vowel_count, current_count)

        return vowel_count

  """
  Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
  """
