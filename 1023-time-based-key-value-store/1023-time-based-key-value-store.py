class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, val: str, timestamp: int) -> None:
        self.store[key].append([val, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l = 0 
        r = len(self.store[key]) - 1

        res = -1
        while l <= r: 
            mid = (l + r) // 2
            if self.store[key][mid][1] <= timestamp: 
                l = mid + 1
                res = mid 
            else: 
                r = mid - 1

        return self.store[key][res][0] if res != -1 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)