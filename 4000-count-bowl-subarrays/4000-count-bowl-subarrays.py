class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        #That is literally a monotonic stack pattern question (missed completely)
        #This is to be noted
        left = [-1] * len(nums)
        right = [len(nums)] * len(nums)

        stack = []
        for i, n in enumerate(nums): 
            idx = -1
            while stack and stack[-1][0] < n:
                #Pop logic to update and right arrays 
                val, idx = stack.pop()
                right[idx] = i

            if stack:
                left[i] = stack[-1][1]

            stack.append((n, i))

        #This is very interesting , if condition is true due to constraint, of unique element, we are gauranteed to be incrementing !!
        ans = 0
        zipped = list(zip(left, right))
        for i in range(len(zipped)): 
            leftGreater, rightGreater = zipped[i]
            if leftGreater != -1 and rightGreater != len(nums): 
                ans += 1

        return ans

        # stack = []
        # stack = []
        # for i in range(len(nums)): 

