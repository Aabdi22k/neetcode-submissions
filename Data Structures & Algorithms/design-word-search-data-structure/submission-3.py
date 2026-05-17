class TrieNode:
    def __init__(self, val='*'):
        self.val = val
        self.children = {}
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode(ch)
            cur = cur.children[ch]
        cur.children['*'] = TrieNode()


    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root

            for j in range(i, len(word)):
                ch = word[j]
                if ch == '.':
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return '*' in cur.children

        return dfs(0, self.root)

        