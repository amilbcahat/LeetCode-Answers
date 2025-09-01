class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Claude Explanations - https://claude.ai/share/587917aa-17a7-480d-afec-4e8d6732b470

        max_num = max(nums)
        msb = max_num.bit_length() - 1 
        max_mask = (1 << (msb + 1)) - 1

        dp = [0] * (max_mask + 1)

        for num in nums: 
            dp[num] = num 

        for bit in range(msb + 1): 
            for mask in range(max_mask + 1): 
                if mask & (1 << bit): 
                    without_bit_set_mask = mask ^ (1 << bit)
                    if dp[mask] < dp[without_bit_set_mask]: 
                        dp[mask] = dp[without_bit_set_mask]

        max_prod = 0
        for num in nums: 
            complement = max_mask ^ num 
            partner = dp[complement]
            if partner > 0: 
                max_prod = max(max_prod, num * partner)

        return max_prod
