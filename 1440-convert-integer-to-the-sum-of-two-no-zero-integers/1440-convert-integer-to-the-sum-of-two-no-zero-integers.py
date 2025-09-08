class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        #straight enumeration
        for i in range(n + 1):
            if '0' not in str((n - i)) and '0' not in str((n - (n - i))):
                return [n - i, n - (n - i)]