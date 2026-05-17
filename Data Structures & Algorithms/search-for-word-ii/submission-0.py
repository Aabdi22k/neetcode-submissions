class TrieNode:
    def __init__(self):
        self.idx = -1
        self.children = [None] * 26
            
class NewTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str, i) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.idx = i
    
    def getRoot(self):
        return self.root
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Trie = NewTrie()

        for i, word in enumerate(words):
            Trie.addWord(word, i)
        

        ROWS, COLS = len(board), len(board[0])
        res = []

        def getIndex(ch):
            return ord(ch) - ord('a')
        
        def backtrack(r, c, cur):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == '#' or 
                not cur.children[getIndex(board[r][c])]): return

            tmp = board[r][c]
            board[r][c] = '#'

            cur = cur.children[getIndex(tmp)] 
            if cur.idx != -1:
                res.append(words[cur.idx])
                cur.idx = -1


            backtrack(r + 1, c, cur)
            backtrack(r - 1, c, cur)
            backtrack(r, c + 1, cur)
            backtrack(r, c - 1, cur)

            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, Trie.getRoot())


        return res



