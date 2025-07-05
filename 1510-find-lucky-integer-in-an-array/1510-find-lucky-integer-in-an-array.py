class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqMap = Counter(arr)
        ans = -1 
        for n in arr: 
            if n in freqMap and freqMap[n] == n: 
                ans = max(ans , n)

        return ans