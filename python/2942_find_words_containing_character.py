class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, v in enumerate(words):
            if x in v:
                ans.append(i)
        
        return ans