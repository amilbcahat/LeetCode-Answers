class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indexMap = defaultdict(list)
        maxDis = float("-inf")

        for i, c in enumerate(s) : 
            indexMap[c].append(i)
            val = indexMap[c]
            if len(val) >= 2 : 
                maxDis = max(maxDis , (val[-1] - val[0] + 1) - 2)

        return maxDis if maxDis != float("-inf") else -1