class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        #preprocess 
        user_to_lang = defaultdict(set)
        for i in range(len(languages)): 
            user_to_lang[i + 1] = set(languages[i])

        #caculate bad users 
        bad_users = set()
        for u1, u2 in friendships: 
            lang1 = user_to_lang[u1]
            lang2 = user_to_lang[u2]
            if not lang1.intersection(lang2): 
                bad_users.add(u1)
                bad_users.add(u2)

        if not bad_users: 
            return 0

        #most spoken language among bad users 
        lang_count = defaultdict(int)
        max_cnt = 0
        for user in bad_users:
            for language in user_to_lang[user]: 
                lang_count[language] += 1
                max_cnt = max(max_cnt, lang_count[language])

        #lang count 
        return len(bad_users) - max_cnt