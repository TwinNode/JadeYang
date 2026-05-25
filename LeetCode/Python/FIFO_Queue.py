class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)    

        while self.queue[0] < t-3000:
            self.queue.pop(0)

        return len(self.queue)

# Pythonic - deque
from collections import deque

def __init__(self):
  self.q = []

def ping(self, t:int) -> int:
  self.q.append(t)
  while self.q[0] < t-3000:
    self.q.popleft()

  return len(self.q)
