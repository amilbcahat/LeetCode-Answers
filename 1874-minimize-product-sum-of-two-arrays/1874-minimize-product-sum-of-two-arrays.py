class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)

        print(nums1, nums2)

        total = 0
        for n1, n2 in zip(nums1, nums2):
            total += (n1 * n2)

        return total