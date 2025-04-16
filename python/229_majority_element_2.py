class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        # boyer moore but track two elements at once. candidates 1 and 2 won't be set to the same element because of the 'elif'
        for i, v in enumerate(nums):
            if v == candidate1:
                count1 += 1
            elif v == candidate2:
                count2 += 1
            elif 0 == count1:
                count1 = 1
                candidate1 = v
            elif 0 == count2:
                count2 = 1
                candidate2 = v
            else:
                count1 -= 1
                count2 -= 1
        
        bound = len(nums) // 3
        c1 = 0
        c2 = 0
        for i,v in enumerate(nums):
            if v == candidate1:
                c1 += 1
            elif v == candidate2:
                c2 += 1
        res = []
        if c1 > bound:
            res.append(candidate1)
        if c2 > bound:
            res.append(candidate2)
        
        return res
