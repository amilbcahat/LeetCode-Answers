class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        save = nums.copy()
        indexMap = {}

        for i , n in enumerate(nums):
            if n not in indexMap : 
                indexMap[n] = i

        
        nums.sort()
        sortedIndexMap = {}
        for i , n in enumerate(nums):
            if n not in sortedIndexMap : 
                sortedIndexMap[n] = i 
        
        ans = [0] * len(save)

        print(nums , save,sortedIndexMap,indexMap)
        for i in range(len(save)):
            ans[i] = sortedIndexMap[save[i]]

        return ans


