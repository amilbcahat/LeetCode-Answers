class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        #Uses Difference Array concept
        for start, end in queries: 
            diff[start] += 1 
            diff[end + 1] -= 1

        curr = diff[0]
        for i in range(1, len(diff)): 
            diff[i] += curr
            curr = diff[i]

        for i in range(len(diff) - 1):
            nums[i] -= diff[i]
            if nums[i] > 0: 
                return False

        return True