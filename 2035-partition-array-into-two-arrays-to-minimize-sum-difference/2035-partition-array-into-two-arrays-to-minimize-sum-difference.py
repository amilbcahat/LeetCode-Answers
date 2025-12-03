import bisect 
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        total = sum(nums)
        left, right = set(), set()
        n = len(nums)

        aL = nums[:(n // 2)]
        aR = nums[(n // 2):]

        left, right = [], []
        leftMap, rightMap = defaultdict(list), defaultdict(list)

        m = len(aL)
        for mask in range(1 << m): 
            cur_sum = 0
            count = 0 
            for j in range(m):
                if (mask >> j) & 1: 
                    cur_sum += aL[j]
                    count += 1

            left.append((cur_sum, count))
            leftMap[count].append(cur_sum)
        
        m = len(aR)
        for mask in range(1 << m): 
            cur_sum = 0
            count = 0 
            for j in range(m):
                if (mask >> j) & 1: 
                    cur_sum += aR[j]
                    count += 1
            right.append((cur_sum, count))
            rightMap[count].append(cur_sum)

        for key in rightMap: 
            rightMap[key].sort()

        for key in leftMap: 
            leftMap[key].sort()
        # print(right, left, rightMap, leftMap, total / 2)
        ans = float("inf")
        for subSum, count in left: 
            targetIdx = n/2 - count
            
            if not targetIdx in rightMap: 
                continue 

            pos = bisect.bisect_left(rightMap[targetIdx], total / 2 - subSum)

            if pos > 0: 
                leftSum = subSum + rightMap[targetIdx][pos - 1]
                rightSum = total - leftSum
                # print("debug", subSum,targetIdx, rightMap[targetIdx], pos, rightSum, leftSum - rightSum  )

                ans = min(ans, abs(leftSum - rightSum))

            if pos < len(rightMap[targetIdx]): 
                leftSum = subSum + rightMap[targetIdx][pos]
                rightSum = total - leftSum
                # print("debug", subSum,targetIdx, rightMap[targetIdx][pos], rightSum,leftSum - rightSum  )
                ans = min(ans, abs(leftSum - rightSum))

        for subSum, count in right: 
            targetIdx = n/2 - count
            
            if not targetIdx in leftMap: 
                continue 

            pos = bisect.bisect_left(leftMap[targetIdx], total / 2 - subSum)

            if pos > 0: 
                rightSum = subSum + leftMap[targetIdx][pos - 1]
                leftSum = total - rightSum
                # print("debug", subSum,targetIdx, leftMap[targetIdx][pos - 1], rightSum, leftSum - rightSum  )

                ans = min(ans, abs(leftSum - rightSum))

            if pos < len(leftMap[targetIdx]): 
                rightSum = subSum + leftMap[targetIdx][pos]
                leftSum = total - rightSum
                # print("debug", subSum,targetIdx, leftMap[targetIdx][pos], rightSum,leftSum - rightSum  )
                ans = min(ans, abs(leftSum - rightSum))
              
        return ans
