class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        #Non overlapping intervals
        res = 0 
        prev = pairs[0]
        for i in range(1, len(pairs)): 
            cur = pairs[i]
            if cur[0] <= prev[1]: 
                res += 1
                prev = [
                cur[0] #prev[0] works fine too here
                , min(prev[1], cur[1])
                ]
            else:
                prev = cur 
        return len(pairs) - res