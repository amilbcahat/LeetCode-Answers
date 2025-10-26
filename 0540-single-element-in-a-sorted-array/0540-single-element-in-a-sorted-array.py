class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #Answer is always where length is odd of search space
        l = 0 
        r = len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2
            if (mid + 1 < len(nums) and nums[mid] != nums[mid + 1]) and (mid - 1 >= 0 and nums[mid] != nums[mid - 1]) or (r - l + 1) == 1: 
                #Ans is here, when length is 1 length case odd 
                return nums[mid]

            else: 
                #Set pointer to count length
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]: 
                    mid += 1

                cur_length_start = (mid - l + 1)
                if cur_length_start % 2 == 0: 
                    l = mid + 1
                else: 
                    #Skip the same element, and move to odd search space, leaving this element
                    mid -= 1
                    r = mid - 1


        
