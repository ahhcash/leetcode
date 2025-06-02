class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word: str):
        curr = self.root
        for c in word:
            child = curr.children.get(c)
            if not child:
                child = Node()
                curr.children[c] = child
            curr = child
        curr.end = True
    
    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(i, node):
            if not node:
                return False
            if i == n:
                return node.end
            c = word[i]
            if not c == ".":
                child = node.children.get(c)
                return dfs(i+1, child)
            else:
                for a in range(26):
                    ch = chr(ord('a') + a)
                    child = node.children.get(ch)
                    if dfs(i+1, child): return True
                return False

        return dfs(0, self.root)

    
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)