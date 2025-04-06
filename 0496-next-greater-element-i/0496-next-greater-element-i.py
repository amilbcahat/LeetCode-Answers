class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Use monotonic stack
        
        stack = []
        track = defaultdict(int)
        for i, n in enumerate(nums2): 
            while stack and stack[-1] < n: 
                elem = stack.pop()
                track[elem] = i
            stack.append(n)

        for ind, n in enumerate(nums1): 
            if n in track: 
                nums1[ind] = nums2[track[n]]
            else:
                nums1[ind] = -1

        return nums1
        