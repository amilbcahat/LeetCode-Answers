class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cache = {}
        def dfs(i, modifiedArr): 
            if modifiedArr == nums2: 
                return i 

            if i == len(nums1): 
                return len(nums1)

            if (i, tuple(modifiedArr)) in cache: 
                return cache[(i, tuple(modifiedArr))]
            best = n
            for s in range(len(modifiedArr)): 
                for e in range(s, len(modifiedArr)): 
                    split = modifiedArr[s: e + 1]
                    r = modifiedArr[:s] + modifiedArr[e + 1:]
                    for k in range(len(r)):
                        best = min(best, dfs(i + 1, r[:k] + split + r[k:]))

            cache[(i, tuple(modifiedArr))] = best

            return best

        return dfs(0, nums1)