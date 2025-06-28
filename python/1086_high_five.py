class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for i, score in items:
            heappush(scores[i], -score)
        n = len(scores)
        res = []
        for i, ss in scores.items():
            avg = 0
            for _ in range(5):
                avg += (-heappop(ss))
            res.append([i, avg//5])
        
        return sorted(res, key=lambda x: x[0])