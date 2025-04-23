class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = defaultdict(int)
        for i in range(1, n + 1):
            total = sum(list(map(int, str(i))))
            hashmap[total] += 1

        maxVal = max(hashmap.values())

        res = 0 
        for key in hashmap: 
            if hashmap[key] == maxVal: 
                res += 1

        return res