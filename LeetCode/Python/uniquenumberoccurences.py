class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        newarr = {k: arr.count(k) for k in arr}

        return len(newarr) == len(set(newarr.values()))

#minimize memory usage ---------------------
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
            # if key 'x' exist, return its value; if not, return 0.
            # then add 1 to update the count

        return len(freq) == len(set(freq.values()))

# use Counter library -------------------------
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        return len(counts) == len(set(counts.values()))
