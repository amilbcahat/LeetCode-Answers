class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        windowSum = cardPoints[0]
        sumOfPoints = sum(cardPoints)
        ans = float('-inf')
        n = len(cardPoints)
        lenOfWin = n - k
        for r in range(1, n):
            if r - l + 1 == lenOfWin + 1: 
                windowSum -= cardPoints[l]
                l += 1
            windowSum += cardPoints[r]
            if r - l + 1 == lenOfWin: 
                ans = max(ans, sumOfPoints - windowSum)

        return ans if windowSum != sumOfPoints else windowSum



