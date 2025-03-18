class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        #Let use Binary Search again O(n ^ 2 * log n) !!!
        #Check for every length , if found maximise that 
        l = 0 
        r = len(nums)
        res = 1
        def can_form_nice_subarray(length): 
            for start in range(len(nums) - length + 1): 
                bit_mask = 0 
                is_nice = True
                for pos in range(start, start + length): 
                    if bit_mask & nums[pos] != 0: 
                        is_nice = False
                        break 
                    bit_mask |= nums[pos]

                if is_nice: 
                    return True
            return False

        while l <= r: 
            mid = (l + r) // 2 
            if can_form_nice_subarray(mid): 
                res = mid 
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        #Logic is simple , if a number has some set bit , then at that place you cant have a set bit O(n)
        # used_bits = 0 
        # res = 0
        # l = 0
        # for r in range(len(nums)): 
        #     while used_bits & nums[r] != 0: 
        #         used_bits ^= nums[l]
        #         l += 1

        #     used_bits |= nums[r]
        #     res = max((r - l + 1), res)
        # return res

            