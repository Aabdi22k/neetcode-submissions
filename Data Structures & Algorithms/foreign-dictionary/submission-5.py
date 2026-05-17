class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {ch: set() for word in words for ch in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            ml = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:ml] == w2[:ml]: 
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        res = []
        visited = {}
        
        def dfs(v):
            if v in visited: return visited[v] == 1

            visited[v] = 1

            for e in adj[v]:
                if dfs(e): return True
            
            visited[v] = 2
            res.append(v)

        for ch in adj:
            if dfs(ch):
                return ""
                
        res.reverse()
        return ''.join(res)
                

