class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator: return "0"

        res = []
        seen = {}
        if numerator * denominator < 0:
            res.append("-")
        
        num, denom = abs(numerator), abs(denominator)
        res.append(str(num//denom))
        num %= denom
        
        if not num: return "".join(res)

        res.append(".")
        while num:
            if num in seen:
                res.insert(seen[num], "(")
                res.append(")")
                break
            seen[num] = len(res)
            num *= 10
            res.append(str(num//denom))
            num %= denom
        
        return "".join(res)

