class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] #maxHeap of bricks 
        #use bricks , and when finished with bricks , with help of 
        #maxHeap , find the largest brick diff used for jumping , and exchange that with ladders
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0 : 
                continue 
            
            bricks -= diff 
            #Push diffs 
            heapq.heappush(heap , -diff)
            if bricks < 0 : 
                #negative bricks , indicate , no more bricks 
                if ladders == 0 :
                    #If not more bricks , then return i , as we cant make a jump from here  
                    return i 
                #Otherwise decrement ladders
                ladders -= 1
                #Exchanged ladder with bricks basically
                bricks += -heapq.heappop(heap)
        #if not stopped , earlier then that means we reached the last building 
        return len(heights) - 1

        # DP (MLE) Solution -> 
        # cache = {}
        # def dfs(i, curBricks , curLadders):
        #     if curBricks == 0 and curLadders == 0 : 
        #         print(heights[i])
        #         return i 

        #     if i == len(heights) - 1:
        #         print(heights[i])
        #         return i

        #     if (i , curBricks , curLadders) in cache : 
        #         return cache[(i , curBricks , curLadders)]

        #     #Take this building into account !
        #     # By initializing res to i at the start of each recursive call, we ensure that res always represents the furthest building index reached at that point in the recursion, even before considering whether to move to the next building using bricks or ladders.
        #     res = i
        #     if heights[i + 1] < heights[i]:
        #         res= max(res , dfs(i + 1  , curBricks , curLadders))
        #     else: 
        #         #Choose bricks 
        #         if curBricks >= (heights[i + 1] - heights[i]): 
        #             res= max(res ,dfs(i + 1 , curBricks - (heights[i + 1] - heights[i]) , curLadders))
        #         #Or Choose Ladder
        #         if curLadders > 0 :
        #             res= max(res ,dfs(i + 1 , curBricks , curLadders - 1))

        #     # print(i , heights[i] , curBricks , curLadders , res)
        #     cache[(i , curBricks , curLadders)] = res 
        #     return res
        # return dfs(0, bricks , ladders)
            