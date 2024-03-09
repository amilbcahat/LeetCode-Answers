class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0 
        stack = []
        prefix = [0]

        for n in nums : 
            prefix.append(prefix[-1] + n)

        #Stack for ascertaining what is the minValue at that point of index
        for i , n in enumerate(nums):
            newStart = i 
            while stack and stack[-1][1] > n : 
                #Pop means the value was minimum for a small part of array , and then there was new minimum for that subarray 
                start , val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res , val * total)
                #When new minmum is ascertained , the starting index of that subarray remains same 
                newStart = start
            stack.append((newStart , n))

        for start , val in stack : 
            #These are values that remain minimum from the start index to the last of subarray 
            total = prefix[len(nums)] - prefix[start]
            res = max(res , val * total)

        #  Return these values 
        return res % (10 ** 9 + 7)