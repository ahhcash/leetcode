class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # first let's try to store all the visited sites for a user sorted by timestamp
        uservisits = defaultdict(list)

        visits = sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1]))

        for user, _, site in visits:
            uservisits[user].append(site)
        
        patterns = Counter()

        for user, sitelist in uservisits.items():
            # Counter#update merges two counter dicts
            # itertools.combinations returns a generator of all combinations of the specified size (3 in this case)
            # we consume the generator by wrapping it with a set(...), and create a counter out of this
            patterns.update(Counter(set(itertools.combinations(sitelist, 3))))
        
        patterns = sorted(patterns.items(), key = lambda x: (-1*x[1], x[0]))
        return patterns[0][0]
