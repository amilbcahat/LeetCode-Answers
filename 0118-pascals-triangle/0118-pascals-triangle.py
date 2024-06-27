class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res  = [[1]]
        #numRows-1 because we already made the first Row 
        for i in range(numRows -1):
            temp = [0] + res[-1] + [0]
            newRow = []
            #newRow length will be 1 one more than the previous Row 
            for j in range(len(res[-1])+1):
                newRow.append(temp[j] + temp[j+1])
            res.append(newRow)
        
        return res 