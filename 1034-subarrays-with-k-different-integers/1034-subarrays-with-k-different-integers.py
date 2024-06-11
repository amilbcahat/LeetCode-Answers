class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atmost(k): 
            l = 0 
            res = 0 
            countMap = defaultdict(int)
            distinct = set()
            for r in range(len(nums)):
                elem = nums[r]
                countMap[elem] += 1
                distinct.add(elem)
                # print(distinct, l)
                while l <= r and len(distinct) > k : 
                    # print(nums[l : r + 1])
                    countMap[nums[l]] -= 1 
                    if countMap[nums[l]] == 0 : 
                        distinct.remove(nums[l])
                    l += 1 

                # print(nums[l : r + 1])
                res += (r - l + 1)

            return res 

        #Count of SubArrays with K Distinct Elements = Count of SubArrays with At Most K Distinct Elements - Count of SubArrays with At Most K-1 Distinct Elements
        return (atmost(k) - atmost(k - 1))
        # return (atmost(k) - atmost(k - 1))