class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        sp = []
        for phrase in phrases:
            phrase = phrase.split(" ")
            sp.append([phrase[0], phrase[-1]])      

        n = len(phrases)
        m = set()
        for i in range(n):
            for j in range(n): 
                if i == j: 
                    continue
                elif sp[i][1] == sp[j][0]:
                    m.add(phrases[i][:-len(sp[j][0])]  + phrases[j])

        return sorted(list(m))
