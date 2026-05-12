class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            for ch in s:
                otherch = chr(ord(ch) + 10)
                res += ch
                res += otherch
            res += '*1/6a87$i31'
        return res
        
    def decode(self, s: str) -> List[str]:
        s = s.split('*1/6a87$i31')
        res = ['' for i in range(len(s) - 1)]
        for i, st in enumerate(s):
            for j in range(0, len(st), 2):
                res[i] += st[j]

        return res
