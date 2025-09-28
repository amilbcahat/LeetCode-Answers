class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2: 
            return abs(nums[0] - nums[1])

            
        prefix = [0] * n 

        prefix[0] = nums[0]

        for i in range(1, n): 
            prefix[i] = prefix[i - 1] + nums[i]

        inc = []
        dec = []
        for i in range(n):
            if dec and dec[-1][1] >= nums[n - 1 - i]: 
                break
            dec.append((n - 1 - i, nums[n - 1 - i]))

        for i in range(n):
            if inc and inc[-1][1] >= nums[i]: 
                break
            inc.append((i, nums[i]))

        if not (0 <= (dec[-1][0] - inc[-1][0]) <= 1):
            return -1

        # print(inc, dec)
        l = inc[-1][0]
        r = dec[-1][0]
        if l == r: 
            pivot = l 
            return min(abs(prefix[pivot] - (prefix[n - 1] - prefix[pivot])), abs(prefix[pivot - 1] - (prefix[n - 1] - prefix[pivot - 1])))
        else:
            return abs((prefix[n - 1] - prefix[l]) - prefix[l])
        # indexOfSep = []
        # print(prefix)
        # for i in range(1, n - 1):
        #     if nums[i  - 1] < nums[i] > nums[i + 1]: 
        #         indexOfSep.append(i)
        #     # elif nums[i  - 1] < nums[i] < nums[i + 1]: 
        #     #     continue
        #     # elif nums[i  - 1] > nums[i] > nums[i + 1]:
        #     #     continue
        #     # elif nums[i] == nums[i + 1] and nums[i - 1] < nums[i] and nums[i + 1] < nums[i + 2]: 
        #     #     return abs((prefix[n - 1] - prefix[i - 1]) - prefix[i - 1])
        #     # else:
        #     #     print(nums[i], nums[i  + 1])
        #     #     return -1 

        # if len(indexOfSep) > 1 or not indexOfSep: 
        #     print(indexOfSep)
        #     return -1

        # pivot = indexOfSep[0]
        # # print(pivot)
        # # abs(prefix[pivot - 1] - (prefix[n] - prefix[pivot - 1]))
        return min(abs(prefix[pivot] - (prefix[n - 1] - prefix[pivot])), abs(prefix[pivot - 1] - (prefix[n - 1] - prefix[pivot - 1])))
        