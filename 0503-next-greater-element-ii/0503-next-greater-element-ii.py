class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * (len(nums) + len(nums)) #To handle the circular case
        stack = []
        cur_max = float("-inf")
        cur_ind = -1
        for i, n in enumerate(nums + nums): 
            while stack and stack[-1][0] < n: 
                popNum, popIndx = stack.pop()
                res[popIndx] = n 
            stack.append((n, i))
        return res[:len(nums)]