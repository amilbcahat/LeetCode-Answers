class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def getColSum(idx):
            return sum(row[idx] for row in mat)
        
        countSpecial = 0 
        for row in mat: 
            if sum(row) == 1 : 
                colIndex = row.index(1)
                countSpecial += getColSum(colIndex) == 1

        return countSpecial 