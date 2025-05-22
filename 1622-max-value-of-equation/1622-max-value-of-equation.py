class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        deque = collections.deque()
        maxValue = float('-inf')

        for point in points:
            x, y = point

            # Remove points that are out of the x range (xi - xj > k)
            while deque and x - deque[0][0] > k:
                deque.popleft()

            # Calculate the equation value with the front of the deque
            if deque:
                maxValue = max(maxValue, y + x + deque[0][1] - deque[0][0])

            # Remove points from the back of the deque that are less efficient
            while deque and y - x >= deque[-1][1] - deque[-1][0]:
                deque.pop()

            # Add the current point to the deque
            deque.append((x, y))

        return maxValue