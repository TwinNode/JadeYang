from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_queue = deque()
        d_queue = deque()
        n = len(senate)

        for index, party in enumerate(senate):
            if party == "R" :
                r_queue.append(index)
            else:
                d_queue.append(index)

        while r_queue and d_queue :
            r_idx = r_queue.popleft()
            d_idx = d_queue.popleft()

            if r_idx < d_idx: # Radiant first
                r_queue.append(r_idx + n)
            else:
                d_queue.append(d_idx + n)
                
        return "Radiant" if r_queue else "Dire"


senate = "RDD"
#Output: "Radiant"
sol = Solution()
sol.predictPartyVictory(senate)
