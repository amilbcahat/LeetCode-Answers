class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        #Like Bottom Up Solution
        n = len(prices)
        deque_ = deque()
        deque_.append(n)
        prices = prices + [0]  # Add a dummy fruit with 0 coins to avoid boundary issues.

        # Iterate from the last fruit to the first
        for i in range(n - 1, -1, -1):
            # Calculate the maximum index that can be covered by the current fruit
            maxCoveredIndex = min(n, 2 * i + 2)

            # Remove all elements from the front that are outside the range of current fruit's reward
            while deque_ and deque_[0] > maxCoveredIndex:
                deque_.popleft()

            # Update the cost of the current fruit by adding the minimum cost of reachable fruits
            prices[i] += prices[deque_[0]]

            # Maintain the deque to keep it increasing
            while deque_ and prices[i] < prices[deque_[-1]]:
                deque_.pop()

            # Add the current fruit index to the deque
            deque_.append(i)

        # Return the minimum cost to get all fruits starting from the first one
        return prices[0]