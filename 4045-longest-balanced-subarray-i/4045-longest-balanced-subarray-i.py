class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0
        for i in range(n):
            even, odd = 0, 0
            distinct = defaultdict(int)   
            for j in range(i, n):
                if nums[j] % 2 == 0 and nums[j] not in distinct:
                    even += 1
                if nums[j] % 2 and nums[j] not in distinct:
                    odd += 1

                distinct[nums[j]] += 1
                # print(nums[i: j + 1], even, odd)
                if even == odd and j > i:
                    res = max(res, j - i + 1)
        # print(nums[i: j + 1])

        return res
