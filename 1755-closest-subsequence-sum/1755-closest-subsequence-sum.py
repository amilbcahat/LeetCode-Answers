import bisect
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        aL = nums[:(n // 2)]
        aR = nums[(n//2):]
        left, right = [], []
        m = len(aL)
        for mask in range(1 << m):
            cur_sum = 0
            for j in range(m):
                if (mask >> j) & 1: 
                    cur_sum += aL[j]
            left.append(cur_sum)


        m = len(aR)
        for mask in range(1 << m):
            cur_sum = 0
            for j in range(m):
                if (mask >> j) & 1: 
                    cur_sum += aR[j]
            right.append(cur_sum)

        right.sort()

        # print(left, right)
        ans = float("inf")
        for ll in left:
            temp = right[0]
            l = 0
            r = len(right) - 1

            pos = bisect.bisect_left(right, goal - ll)
            
            if pos < len(right):
                ans = min(ans, abs(ll + right[pos] - goal))
            
            if pos > 0: 
                ans = min(ans, abs(ll + right[pos - 1] - goal))

        #    - right[pos] = 8     → first value >= target
        #     - right[pos-1] = 5   → last value < target

        return ans
