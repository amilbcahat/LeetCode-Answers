class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # preprocess languages array
        user_to_lang = defaultdict(set)
        for i in range(len(languages)):
            user_to_lang[i+1] = set(languages[i])

        # find out which users can't communicate w their friends ("bad")
        bad_users = set()
        for u1, u2 in friendships:
            lang1 = user_to_lang[u1]
            lang2 = user_to_lang[u2]
            if not lang1.intersection(lang2):
                bad_users.add(u1)
                bad_users.add(u2)
        if not bad_users:
            return 0

        # calculate the most spoken language among those bad users
        lang_count = defaultdict(int)
        max_lang_count = 0
        for u in bad_users:
            for lang in user_to_lang[u]:
                lang_count[lang] += 1
                max_lang_count = max(max_lang_count, lang_count[lang])

        # teach the most spoken language to the users who can't speak it and are "bad"
        return len(bad_users) - max_lang_count