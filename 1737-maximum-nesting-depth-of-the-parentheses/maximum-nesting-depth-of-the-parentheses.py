class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0 
        maxCounter = float("-inf")
        for n in s :
            if n == "(" :
                counter += 1 
            elif n == ")":
                counter -= 1

            maxCounter = max(counter , maxCounter)
        return maxCounter
