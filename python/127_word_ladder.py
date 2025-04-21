class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                # skip the ith charatcer, so hot would have neighbors *ot, h*t and ho*.
                p = word[:i] + "*" + word[i+1:]
                graph[p].append(word)
        print(graph)
        q = deque()
        q.append(beginWord)
        level = 1
        vis = set()
        vis.add(beginWord)
        while q:
            s = len(q)
            for i in range(s):
                word = q.popleft()
                for j in range(len(word)):
                    p = word[:j] + "*" + word[j+1:]
                    for nei in graph[p]:
                        if nei == endWord:
                            return level + 1
                        if nei not in vis:
                            vis.add(nei)
                            q.append(nei)
            level += 1
        return 0
