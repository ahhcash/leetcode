class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if not total % k == 0:
            return False
        nums.sort(reverse=True)
        target = total // k
        used = [False] * n

        def dfs(i, remain, curr):
            if remain == 0:
                return True
            
            if curr > target:
                return False
            
            if curr == target:
                return dfs(0, remain - 1, 0)
            
            for j in range(i, n):
                if not used[j]:
                    used[j] = True
                    if dfs(j+1, remain, curr + nums[j]):
                        return True
                    used[j] = False
                    if curr == 0:
                        break
            return False

        return dfs(0, k, 0)
