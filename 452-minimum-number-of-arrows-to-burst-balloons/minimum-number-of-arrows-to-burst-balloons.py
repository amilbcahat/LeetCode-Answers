class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points) # n arrows need to burst n balloons 

        prev = points[0] #contains overlapped section 
        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prev[1] : #overlaps
                res -= 1 #Less arrows need since we have same arrow to intersect more than one balloons 
                prev = [curr[0] , min(curr[1] , prev[1])]
            else : 
                prev = curr 

        return res 



        print(points)