class SegmentTree: 
    def __init__(self, people): 
        n = len(people)
        self.people = people 
        self.tree = [0] * (4 * n)
        self.result = [None] * n 

    def buildTree(self, index, start, end):
        if start == end: 
            self.tree[index] = 1
            return 

        mid = (start + end) // 2
        self.buildTree(2 * index + 1, start, mid)
        self.buildTree(2 * index + 2, mid + 1, end)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def query(self,index, left, right, position, height, originalPos): 
        if left == right: 
            self.result[left] = [height, originalPos]
            self.tree[index] -= 1
            return 

        if self.tree[index] < position: 
            return 

        mid = (left + right) // 2
        if self.tree[2 * index + 1] >= position: 
            self.query(2 * index + 1, left, mid, position, height, originalPos)
        else:
            self.query(2 * index + 2, mid + 1, right, position - self.tree[2 * index + 1], height, originalPos)

        self.tree[index] -= 1

        


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        seg = SegmentTree(people)
        seg.buildTree(0, 0, n - 1)
        
        for p in people: 
            seg.query(0, 0, n - 1, p[1] + 1, p[0], p[1])

        res = seg.result 

        return res