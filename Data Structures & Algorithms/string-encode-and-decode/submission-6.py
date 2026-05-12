class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(s)
            res.append(',#1')
        return ''.join(res)
        


    def decode(self, s: str) -> List[str]:
        res = s.split(',#1')
        if res[-1] == '':
            res.pop()
        return res