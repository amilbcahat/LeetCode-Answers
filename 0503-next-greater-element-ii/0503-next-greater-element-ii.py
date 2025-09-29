class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * (len(nums) + len(nums))
        stack = []
        for i, n in enumerate(nums + nums): 
            while stack and stack[-1][1] < n: 
                popIdx, popElem = stack.pop()
                res[popIdx] = n

            stack.append((i, n))

        return res[:len(nums)]