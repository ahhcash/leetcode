class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        
        ones = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        def solve(num):
            if num < 10:
                return ones[num]
            elif num < 20:
                return teens[num]
            elif num < 100:
                return tens[(num // 10) * 10] + (" " + solve(num % 10) if not num % 10 == 0 else "")
            elif num < 1000:
                return solve(num // 100) + " Hundred" + (" " + solve(num % 100) if not num % 100 == 0 else "")
            elif num < 1000000:
                return solve(num // 1000) + " Thousand" + (" " + solve(num % 1000) if not num % 1000 == 0 else "")
            elif num < 1000000000:
                return solve(num // 1000000) + " Million" + (" " + solve(num % 1000000) if not num % 1000000 == 0 else "")
            
            return solve(num // 1000000000) + " Billion" + (" " + solve(num % 1000000000) if not num % 1000000000 == 0 else "")
        
        return solve(num)