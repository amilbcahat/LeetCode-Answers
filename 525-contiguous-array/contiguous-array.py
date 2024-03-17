class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #Play with prefix 
        diff_index = {} #ones - zeroes (tells no. of extra 1s)
        zeros , ones = 0 , 0
        res = 0
        for i , n in enumerate(nums):
            if n == 0 : 
                zeros += 1
            else : 
                ones += 1 

            if (ones - zeros) not in diff_index:
                diff_index[ones - zeros] = i

            if ones == zeros : 
                #This means the subarray is longest and starts from the beginning 
                res = ones + zeros
            else:
                #Logic here is very good , suppose we get at a position diff (ones - zeroes)
                #is not zero and we have extra ones , then we would want to remove those
                #Extra ones , from the subarray(which is in current state , starting from
                # from beginning) , so we would want to remove extra ones , and we have diff 
                #in the map , and that diff tells us , where the extra ones and how many extra 
                #ones are , so we chop off that part from subarray and check for equal number
                #of ones and zeroes , we do this till we find the correct result
                idx = diff_index[ones - zeros]
                res = max(res , i - idx)

        return res 