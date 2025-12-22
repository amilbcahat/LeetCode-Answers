class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #Just used a sliding window 
        count = 0 
        #Maintain prefixSum toa avoid TLE 
        curSum = sum(arr[:k-1])
        #k-1 = 2 (2 not included , hence we did not take sum of last element)
        for L in range(len(arr)-k+1):
            curSum += arr[L+k-1]
            #Here we took sum of last element of windows 
            if curSum/k >= threshold :
                count += 1
            curSum -= arr[L]
            #As window moved forward , we remove the last added element 
        return count 