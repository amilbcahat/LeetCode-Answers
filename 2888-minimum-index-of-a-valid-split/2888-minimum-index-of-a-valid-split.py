class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # #Find dominant with Boyer Moore 
        # res, count = 0, 0 
        # xCount = 0
        # for num in nums: 
        #     if count == 0:
        #         res = num 
        #         xCount = 0
        #     count += (1 if res == num else -1)
        
        # #Get count of that dominant
        # for num in nums: 
        #     if num == res: 
        #         xCount += 1

        # c = 0
        # for i in range(len(nums)): 
        #     if res == nums[i]: 
        #         c += 1
        #     indx = i 
        #     #try split 
        #     #left side and right side length should have same dominant elem as dominant in whole of nums
        #     if c > (indx  + 1) / 2 and (xCount - c) > (len(nums) - indx - 1) / 2: 
        #         return indx
        
        # return -1 

        secondMap = Counter(nums)
        firstMap = defaultdict(int)
        for i, num in enumerate(nums): 
            firstMap[num] += 1
            secondMap[num] -= 1

            if (firstMap[num] > (i + 1) / 2) and (secondMap[num] > (len(nums) - i - 1) / 2): 
                return i

        return -1