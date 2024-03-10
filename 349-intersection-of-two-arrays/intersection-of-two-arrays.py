class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        ans = []

        for n in nums2Set : 
            if n in nums1Set:
                ans.append(n)

        return ans