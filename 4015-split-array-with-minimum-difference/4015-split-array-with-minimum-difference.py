class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
            
        prefix = [0] * n 

        prefix[0] = nums[0]

        for i in range(1, n): 
            prefix[i] = prefix[i - 1] + nums[i]

        l = 0 
        r = n - 1
        for rr in range(n - 1, 0, -1):
            # print(nums[r], nums[r - 1])
            if not ((nums[r - 1] > nums[r])): 
                print(nums[r ], nums[r], "r" )
                break
            r = rr

        for ll in range(n - 1):
            if not ((nums[l] < nums[l + 1])):
                print(nums[l], nums[l + 1], "l")
                break
            l = ll


        # print(l, r, "k")

        #Not a valid mountain array
        if not (0 <= (r - l) <= 1):
            return -1

        if l == r: 
            pivot = l 
            return min(abs(prefix[pivot] - (prefix[n - 1] - prefix[pivot])), abs(prefix[pivot - 1] - (prefix[n - 1] - prefix[pivot - 1])))
        else:
            return abs((prefix[n - 1] - prefix[l]) - prefix[l])
