class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        #Solution: https://leetcode.com/problems/maximum-total-from-optimal-activation-order/solutions/7062903/easy-solution
        buckets = defaultdict(list)

        for v, L in zip(value, limit): 
            buckets[L].append(v)
        
        ans = 0
        for L, arr in buckets.items(): 
            arr.sort(reverse=True)
            ans += sum(arr[:L])

        return ans 