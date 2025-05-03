class Solution:        
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps 
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations couldn't be done
                if A[i] != x and B[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif A[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x    
                elif B[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)
    
        n = len(A)
        rotations = check(A[0]) 
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations 
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])
        # countMapT = Counter(tops)
        # countMapB = Counter(bottoms)
        # maxCountT = max(countMapT.values())
        # maxCountB = max(countMapB.values())

        # maxCountVarT = -1 
        # maxCountVarB = -1 

        # for key in countMapT: 
        #     if countMapT[key] == maxCountT: 
        #         maxCountVarT = key

        # for key in countMapB: 
        #     if countMapB[key] == maxCountB: 
        #         maxCountVarB = key

        # opsT = 0 
        # opsB = 0 

        
        # for i in range(len(tops)): 
        #     if tops[i] != maxCountVarT and bottoms[i] == maxCountVarT: 
        #         opsT += 1

        # for i in range(len(bottoms)): 
        #     if bottoms[i] != maxCountVarB and tops[i] == maxCountVarB: 
        #         opsB += 1

        # opsT = -1 if opsT + maxCountT != len(tops) else opsT
        # opsB = -1 if opsB + maxCountB != len(bottoms) else opsB

        # return min(opsB, opsT) if opsT > 0 and opsB > 0 else opsT if opsT > 0 else opsB