class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] #pair: (index, height)

        for i, h in enumerate(heights): 
            start = i 
            while stack and stack[-1][1] > h: 
                #This bar height cant be increased further
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))

                #Push the current height bar extension backwards, as much possible
                start = index 
            stack.append((start, h))


        #Bar heights, which extended till end
        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea 