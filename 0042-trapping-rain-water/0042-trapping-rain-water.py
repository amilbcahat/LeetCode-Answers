class Solution:
    def trap(self, height: List[int]) -> int:
        #Good way to understand - https://claude.ai/public/artifacts/a2290447-5718-432c-8484-d20c0c2f335c

        ans = 0 
        current = 0 
        stack = [] #Monotonic stack to track indicies for longer bars
        while current < len(height): 
            while stack and height[current] > height[stack[-1]]: 
                top = stack[-1] #last longer bar(this means that level under this has been covered for that plothole)
                stack.pop()
                if not stack: 
                    break 

                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top] #We minus height of top to eliminate levels that have already been calculated
                ans += distance * bounded_height
            stack.append(current)
            current += 1

        return ans
                