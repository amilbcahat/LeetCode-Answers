class SegmentTree: 
    def __init__(self, arr): 
        self.n = len(arr)
        self.arr = arr 
        self.tree = [0] * (self.n * 4)

    def buildTree(self,node, start, end): 
        if start == end: 
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.buildTree(2 * node, start, mid)
            self.buildTree(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


    def update(self, node, start, end, idx, val): 
        if start == end:
            self.tree[node] = val 
            self.arr[idx] = val
        else: 
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(2 * node, start, mid, idx, val)
            else:
                self.update(2 * node + 1, mid + 1, end, idx, val)

            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


    def query(self, node, start, end, L, R): 
        if R < start or end < L: 
            return 0 

        if L <= start and end <= R: 
            return self.tree[node]

        mid = (start + end) // 2
        leftSum = self.query(2 * node, start, mid, L, R)
        rightSum = self.query(2 * node + 1, mid + 1, end , L, R)
        return leftSum + rightSum

    

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg = SegmentTree(nums)
        self.seg.buildTree(1, 0,self.n - 1)

    def update(self, index: int, val: int) -> None:
        self.seg.update(1, 0, self.n - 1, index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.seg.query(1, 0, self.n - 1, left, right)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)