class Solution:
    def maxFreqSum(self, s: str) -> int:
        conMap = defaultdict(int)
        vowelMap = defaultdict(int)

        for c in s: 
            if c in 'aeiou':
                vowelMap[c] += 1
            else:
                conMap[c] += 1

        return (max(vowelMap.values()) if vowelMap else 0) + (max(conMap.values()) if conMap else 0)