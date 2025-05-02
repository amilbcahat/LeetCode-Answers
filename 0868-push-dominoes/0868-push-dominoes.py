class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dominoes = list(dominoes)
        last = ['', 0]
        for i, c in enumerate(dominoes):
            if c == 'L': 
                if last[0] == 'R': 
                    l = last[1]
                    r = i 
                    while l < r: 
                        dominoes[l] = 'R'
                        dominoes[r] = 'L'
                        l += 1 
                        r -= 1

                else: 
                    for j in range(last[1], i + 1): 
                        dominoes[j] = 'L'
                last = ['L', i]
            elif c == 'R': 
                if last[0] == 'R': 
                    for j in range(last[1], i + 1): 
                        dominoes[j] = 'R'
                else:
                    pass

                last = ['R', i]

        if last[0] == 'R': 
            for i in range(last[1], len(dominoes)): 
                dominoes[i] = 'R'

        return "".join(dominoes)
            