class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = end = 0

        if not s and t : return True #not neccessary

        while start < len(s) and end < len(t): 
            if (s[start] == t[end]):
                start += 1

            end +=1

        return start == len(s)

  #improved
  class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t) #move on to next value
        return all(char in it for char in s) # all: True only if all conditions met
