class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        if total % 4 != 0: return False
        target = total // 4
        print(f"target: {target}")
        n = len(matchsticks)
        used = [False] * n

        print(f"matchsticks: {matchsticks}")
        def dfs(i, remain, curr):
            if remain == 0: 
                return True
            if curr == target: 
                print(f"used: {[1 if used[i] else 0 for i in range(n)]}")
                return dfs(0, remain - 1, 0)
            if curr > target: return False

            for j in range(i, n):
                if not used[j]:
                    used[j] = True
                    if dfs(j+1, remain, curr + matchsticks[j]):
                        return True
                    used[j] = False
            return False

        return dfs(0, 4, 0)
        