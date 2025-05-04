class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #Represent in Binary 
        ret = 0 
        nums = defaultdict(int)
        for x, y in dominoes: 
            val = x * 10 + y if x <= y else 10 * y + x
            ret += nums[val]
            nums[val] += 1

        return ret