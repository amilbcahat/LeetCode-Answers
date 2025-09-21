class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        #BFS 
        q = deque([(0, nums1)])
        visit = set()
        while q: 
            steps, curr = q.popleft()
            curr = list(curr)
            if curr == nums2: 
                return steps 

            for s in range(len(curr)): 
                for e in range(s, len(curr)): 
                    split = curr[s: e + 1]
                    remainder = curr[:s] + curr[e + 1:]
                    for index in range(len(remainder)): 
                        new_per = tuple(remainder[:index] + split + remainder[index:])
                        if new_per not in visit: 
                            visit.add(new_per)
                            q.append((steps + 1, new_per))


        #DFS
        #Just generate as much as possible
        # n = len(nums1)
        # cache = {}
        # def dfs(i, modifiedArr): 
        #     if modifiedArr == nums2: 
        #         return i 

        #     if i == len(nums1): 
        #         return len(nums1)

        #     if (i, tuple(modifiedArr)) in cache: 
        #         return cache[(i, tuple(modifiedArr))]
        #     best = n
        #     for s in range(len(modifiedArr)): 
        #         for e in range(s, len(modifiedArr)): 
        #             split = modifiedArr[s: e + 1]
        #             r = modifiedArr[:s] + modifiedArr[e + 1:]
        #             for k in range(len(r)):
        #                 best = min(best, dfs(i + 1, r[:k] + split + r[k:]))

        #     cache[(i, tuple(modifiedArr))] = best

        #     return best

        # return dfs(0, nums1)