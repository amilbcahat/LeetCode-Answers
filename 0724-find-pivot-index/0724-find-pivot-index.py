class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = 0
        postfixSum = 0
        arr = []
        for i in range(len(nums)):
            num = nums[i]
            prefixSum += num 
            arr.append(prefixSum)


        for i in range(len(nums) - 1 , -1 , -1):
            num = nums[i]
            postfixSum += num 
            arr[i] -= postfixSum
            
        print(arr)
        for i in range(len(arr)):
            if arr[i] == 0: 
                return i

        return -1 