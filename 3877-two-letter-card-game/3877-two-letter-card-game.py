class Solution:
    def score(self, cards: List[str], x: str) -> int:
        x0_d, x1_d = {}, {}   # frequency maps for cards with x in pos0 and pos1
        x0, x1, jokers = 0, 0, 0

        # classify cards
        for c in cards:
            if x in c:
                if c[0] == x and c[1] == x:   # joker card
                    jokers += 1
                elif c[1] == x:               # x at position 1
                    x1_d[c] = x1_d.get(c, 0) + 1
                    x1 += 1
                elif c[0] == x:               # x at position 0
                    x0_d[c] = x0_d.get(c, 0) + 1
                    x0 += 1

        x0_d = sorted(x0_d.values(), reverse=True)
        x1_d = sorted(x1_d.values(), reverse=True)

        if x0_d: 
            maxx0 = x0_d[0]
            otherx0 = x0 - maxx0
        else: 
            maxx0 = otherx0 = 0

        if x1_d: 
            maxx1 = x1_d[0]
            otherx1 = x1 - maxx1
        else: 
            maxx1 = otherx1 = 0

        if otherx0 >= maxx0: 
            pairsx0 = x0 // 2
            unpairedx0 = x0 % 2
        else:
            pairsx0 = otherx0 
            unpairedx0 = maxx0 - otherx0

        if otherx1 >= maxx1: 
            pairsx1 = x1 // 2
            unpairedx1 = x1 % 2
        else:
            pairsx1 = otherx1 
            unpairedx1 = maxx1 - otherx1

        not_joker_pairs = pairsx0 + pairsx1 

        rem_not_jokers = unpairedx1 + unpairedx0 
        rem_joker_pairs = min(jokers, rem_not_jokers)
        jokers -= rem_joker_pairs

        fix_pairs = min(jokers, not_joker_pairs)
        rem_maximized_pairs = fix_pairs // 2 # addition of pairs 

        return rem_maximized_pairs + rem_joker_pairs + not_joker_pairs
