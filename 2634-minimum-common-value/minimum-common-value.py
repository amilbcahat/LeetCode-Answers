class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #Easy problem 
        l, r = 0 , 0 

        for n in nums1 :
            l , r = 0 , len(nums2) - 1 
            while l <= r :
                mid = (l + r) // 2 
                if nums2[mid] == n : 
                    return n 
                elif nums2[mid] < n : 
                    l = mid + 1 
                elif nums2[mid] > n : 
                    r = mid - 1 
        
        return -1 