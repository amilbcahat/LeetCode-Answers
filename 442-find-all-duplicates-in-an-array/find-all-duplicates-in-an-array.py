class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums : 
            n = abs(n)
            if nums[n - 1] < 0 : 
                res.append(n)

            #Mark visited as negative and add to answer array if negative is found(meaning we already visited that
            #element )
            nums[n - 1] = -nums[n - 1]

        return res 