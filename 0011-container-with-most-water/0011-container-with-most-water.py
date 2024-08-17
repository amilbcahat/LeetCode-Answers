class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0 , len(height) -1 
        res = 0
        while l < r : 
            area = (r - l) * min(height[l] , height[r])
            res = max(area , res)

            #Move for more area , if any height is less , move forward to look for more potentially !
            if height[l] > height[r]:
                r -= 1 
            else: 
                l += 1
        return res 