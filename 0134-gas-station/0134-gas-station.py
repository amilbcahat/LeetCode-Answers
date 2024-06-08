class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Cant reach the reach destination 
        if sum(gas) < sum(cost):
            return -1 

        total = 0 
        res = 0 

        #There is a solution now 
        #Solution is unique , so only one solution , and that is when we have some value 
        #in total (positive) return the start position 

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total += diff

            if total < 0 : 
                total = 0 
                res = i + 1

        return res 
        