class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        leftBound = [-1] * len(arr)
        rightBound = [len(arr)] * len(arr)
        stack = []
        for i, n in enumerate(arr): 
            # print(i, n)
            while stack and stack[-1][0] > n: 
                popElem, popIndex = stack.pop()
                rightBound[popIndex] = i 
            if stack: 
                leftBound[i] = stack[-1][1]
            stack.append((n, i))

        res = 0
        for i, n in enumerate(arr): 
            no_of_right_sub = rightBound[i] - i
            no_of_left_sub = i - leftBound[i]
            res += (no_of_right_sub * no_of_left_sub * arr[i]) 

        return res % MOD



