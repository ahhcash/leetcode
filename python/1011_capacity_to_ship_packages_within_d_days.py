class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysToShip(shipWeight):
            total = 0
            days = 1
            for i,v in enumerate(weights):
                if total + v <= shipWeight:
                    total += v
                else:
                    days += 1
                    total = v
            return days
        
        l, r = max(weights), sum(weights)
        res = l
        while l <= r:
            m = (l + r) // 2
            d = daysToShip(m)
            if d <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
            # else:
                # r = m - 1
        
        return res