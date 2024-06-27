class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1 )
            #inner loop will iterate till previous row length 
            for j in range(len(res)):
                #Filling children from parent 
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            
            res = next_row
        
        return res 