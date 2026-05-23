class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            while stack and stack[-1] > 0 and x < 0:  
              #collision happens only when last value of stack(stack[-1]) is positive, and incoming value(x) is negative
                if abs(stack[-1]) > abs(x) :
                    break # to leave the while-loop and go to else
                elif abs(stack[-1]) < abs(x):
                    stack.pop()
                    continue # to go back to while-loop to compare again
                elif abs(stack[-1]) == abs(x):
                    stack.pop()
                    break
            else:
                stack.append(x)

        return stack
