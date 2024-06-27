class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        countMap = Counter(s)

        return (countMap['1'] - 1) * '1' + (countMap['0'] * '0') + "1" 