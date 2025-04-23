class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            # w * log(w) if average word length is w
            sorted_word = ''.join(sorted(word))

            res[sorted_word].append(word)
        
        ans = []
        for k, v in res.items():
            ans.append(v)
        return ans