class SegmentTree: 
    def __init__(self, ratings): 
        self.n = ratings
        self.LeftTree = [0] * (4 * ratings)
        self.RightTree = [0] * (4 * ratings)

    def update(self, index, val, start, end, tree, position): 
        if start == end: 
            tree[index] += val 
        else: 
            mid = (start + end) // 2 
            if position <= mid: 
                self.update(2 * index + 1, val, start, mid, tree, position)
            else: 
                self.update(2 * index + 2, val, mid + 1, end, tree, position)
            tree[index] = tree[2 * index + 1] + tree[2 * index + 2]

    def sumRange(self, index, L, R, start, end, tree):
        if start >= L and end <= R: 
            return tree[index]

        if R < start or L > end: 
            return 0 

        mid = (start + end) // 2
        leftSum = self.sumRange(2 * index + 1, L, R, start, mid, tree)
        rightSum = self.sumRange(2 * index + 2, L, R, mid + 1, end, tree)
        return leftSum + rightSum


class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        maxRatings = max(ratings) + 1
        seg = SegmentTree(maxRatings) 
        teamCount = 0
        #Update Right tree
        for i in range(1, len(ratings)): 
            seg.update(0, 1, 0, seg.n - 1, seg.RightTree, ratings[i])

        seg.update(0, 1, 0, seg.n - 1, seg.LeftTree, ratings[0])

        for i in range(1, len(ratings)): 
            # for 1 < 2 < 3
            leftLessCount = seg.sumRange(0, 0, ratings[i] - 1, 0, seg.n - 1, seg.LeftTree)
            rightGreaterCount = seg.sumRange(0, ratings[i] + 1, maxRatings - 1, 0, seg.n - 1, seg.RightTree)
            teamCount += (leftLessCount * rightGreaterCount)

            # for 4 > 2 > 1 
            leftGreaterCount = seg.sumRange(0, ratings[i] + 1, maxRatings - 1, 0, seg.n - 1, seg.LeftTree)
            rightLessCount = seg.sumRange(0, 0, ratings[i] - 1, 0, seg.n - 1, seg.RightTree)
            teamCount += (leftGreaterCount * rightLessCount)


            seg.update(0, 1, 0, seg.n - 1, seg.LeftTree, ratings[i])
            seg.update(0, -1, 0, seg.n - 1, seg.RightTree, ratings[i])

        return teamCount