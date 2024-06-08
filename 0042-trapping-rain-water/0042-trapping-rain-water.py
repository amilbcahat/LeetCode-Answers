class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : 
            return 0 
        l , r = 0 , len(height) - 1
        leftMax , rightMax = height[l], height[r] #moves on pointer 
        res = 0 

        #Notice that we just need sum of min(l , r) - height[i]
        #We take two pointer , we check which leftMax or rightMax is less , then add to sum
        #It works just like min(l , r) , as if leftMax < rightMax , then we can surely , say that
        #l had been smaller than some R on the right 
        while l < r : 
            #leftMax and rightMax are different than in last solution 
            if leftMax < rightMax : 
                l += 1 
                leftMax = max(leftMax , height[l])
                res += (leftMax - height[l])
            else:
                r -= 1 
                rightMax = max(rightMax , height[r])
                res += (rightMax - height[r])

        return res 


        # n = len(height)

        # if n==0 : 
        #     return 0 
        
        # left = [0]*n
        # right = [0]*n 
        # water = 0 
        # left[0] = height[0]

        # for i in range(1,n):
        #     left[i] = max(left[i-1],height[i])
        
        # right[n-1] = height[n-1]
        
        # for i in range(n-2,-1,-1):
        #     right[i] = max(right[i+1],height[i]) 

        # for i in range(0 ,n):
        #     # print(min(left[i], right[i]))
        #     water += min(left[i], right[i]) -height[i]

        # # print(height)
        # # print(left)
        # # print(right)
        # return water 