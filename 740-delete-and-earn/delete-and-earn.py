class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        #We sort and remove duplicates 
        nums = sorted(list(set(nums)))

        #We use house robber problem concept (shifts like fibonacci)
        # e1 , e2 ,     curEarn 
        #[1 ,   3 ,       4         ]
        #We will compute such that , the computed value will show the largest earned value possible at that point(index)
        #in that array !
        earn1 , earn2 = 0 , 0 
        for i in range(len(nums)):
            #We just need to see the previous two values , to evaluate this 
            curEarn = nums[i] * count[nums[i]]
            #Cant use both curEarn and earn2 and they have only one difference value !
            if i > 0 and nums[i] == nums[i - 1] + 1: 
                #if condition not follow then we look prev to prev value and see if it is a possible solution 
                #Two subproblems are including curEarn and earn1 (prev to prev value) or just the prev value 
                temp = earn2 
                earn2 = max(curEarn + earn1 , earn2)
                earn1 = temp
            else : 
                #If not prev elem is not 1 less than curElem , then we can take the prev value(earn2) with curEarn
                # or prev to prev value with curEarn
                #We here just take the prev value , because prev value will have the largest earn value till that point(index)
                #in array   
                print(i ,earn1 , earn2 , curEarn)
                temp = earn2 
                earn2 = curEarn + earn2 
                earn1 = temp 

        return earn2 