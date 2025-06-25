class SegmentTree: 
    def __init__(self,start, end, xArray): 
        self.left = None 
        self.right = None 
        self.total = 0 
        self.xArray = xArray
        self.start = start
        self.end = end 
        self.count = 0 

    def getRangeMid(self): 
        return (self.start + self.end) // 2

    def getLeft(self): 
        if self.left is None: 
            self.left = SegmentTree(self.start, self.getRangeMid(), self.xArray)
        return self.left


    def getRight(self): 
        if self.right is None: 
            self.right = SegmentTree(self.getRangeMid(), self.end, self.xArray)
        return self.right

    def update(self,i, j, val): 
        if i >= j: 
            return 0 
        
        if self.start == i and self.end == j: 
            self.count += val
        else: 
            self.getLeft().update(i, min(self.getRangeMid(), j), val)
            self.getRight().update(max(self.getRangeMid(), i), j, val)

        if self.count > 0: 
            self.total = self.xArray[self.end] - self.xArray[self.start]
        else: 
            self.total = self.getLeft().total + self.getRight().total
        return self.total




class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN = 1
        CLOSE = -1 
        events = []
        xCoordinates = set()
        for rectangle in rectangles: 
            if rectangle[0] < rectangle[2] and rectangle[1] < rectangle[3]: 
                events.append([rectangle[1], OPEN, rectangle[0], rectangle[2]])
                events.append([rectangle[3], CLOSE, rectangle[0], rectangle[2]])
                xCoordinates.add(rectangle[0])
                xCoordinates.add(rectangle[2])

        xArray = sorted(xCoordinates)
        xIndexMap = {x: i for i, x in enumerate(xArray)}

        segmentTree = SegmentTree(0, len(xArray) - 1, xArray)
        currentY = events[0][0]
        currentXSum = 0
        totalArea = 0
        events.sort(key=lambda x: x[0])
        for event in events: 
            y, eventType, x1, x2 = event

            totalArea += (y - currentY) * currentXSum

            currentXSum = segmentTree.update(xIndexMap[x1], xIndexMap[x2], eventType)


            currentY = y 

        MOD = 10 ** 9 + 7
        return totalArea % MOD