class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1 , -1 , -1):
            for j in range(i + 1 , len(nums)):
                if nums[i] < nums[j]:
                    #Check with prev element (who are bigger than current element)
                    #If found then we take max of current (to compare all conditions) and 1 + prev elem subproblem
                    #1 + is done to account for the added length and updated value !
                    LIS[i] = max(LIS[i] , 1 + LIS[j])

        print(LIS)
        #LIS[0] is not taken because , it is possible tha nums[i] < nums[j] does not hold everytime , so we mess up the 
        #solution , and solution can be anywhere in the array !
        return max(LIS)