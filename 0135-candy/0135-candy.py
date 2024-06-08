class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings)
        #Kinda like prefix and postfix 

        #Give initial values , based on default 1 value 

        for i in range(1 , len(ratings)):
            if ratings[i] > ratings[i - 1] : 
                arr[i] = arr[i - 1] + 1 

        #Max in second pass , so that assumed 1 positions are filled out as well 
        
        for i in range(len(ratings) - 2 , -1 , -1):
            if ratings[i] > ratings[i + 1] : 
                arr[i] = max(arr[i] , arr[i + 1] + 1)

        return sum(arr)