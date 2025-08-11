class Solution:
    def __init__(self):
        self.memo_cuts = []
        self.memo_palindrome = []

    def minCut(self, s: str) -> int:
        self.memo_cuts = [None] * len(s)
        self.memo_palindrome = [[None] * len(s) for _ in range(len(s))]
        return self.find_minimum_cut(s, 0, len(s) - 1, len(s) - 1)

    def find_minimum_cut(
        self, s: str, start: int, end: int, minimum_cut: int
    ) -> int:
        # base case
        if start == end or self.is_palindrome(s, start, end):
            return 0
        # check for results in memo_cuts
        if self.memo_cuts[start] is not None:
            return self.memo_cuts[start]
        for current_end_index in range(start, end + 1):
            if self.is_palindrome(s, start, current_end_index):
                minimum_cut = min(
                    minimum_cut,
                    1
                    + self.find_minimum_cut(
                        s, current_end_index + 1, end, minimum_cut
                    ),
                )
        self.memo_cuts[start] = minimum_cut
        return minimum_cut

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        if start >= end:
            return True
        # check for results in memo_palindrome
        if self.memo_palindrome[start][end] is not None:
            return self.memo_palindrome[start][end]
        self.memo_palindrome[start][end] = s[start] == s[
            end
        ] and self.is_palindrome(s, start + 1, end - 1)
        return self.memo_palindrome[start][end]