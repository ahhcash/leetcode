class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        def vow(w):
            for c in w:
                if c in vowels: return True
            return False
        
        def cons(w):
            for c in w:
                if not c.isdigit() and c not in vowels: return True
            return False

        # print(f"cons: {cons(word)}")
        return len(word) >= 3 and vow(word) and cons(word) and word.isalnum()