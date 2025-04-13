class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore majority vote
        candidate, count = 0, 0
        for i, v in enumerate(nums):
            if i == 0:
                candidate = v
                count = 1
            elif v == candidate:
                count += 1
            else:
                count -= 1
                if 0 >= count:
                    candidate = v
                    count = 1
        return candidate