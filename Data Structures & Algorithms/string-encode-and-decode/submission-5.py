class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += s
            res += ',#1'
        print(res)
        return res
        


    def decode(self, s: str) -> List[str]:
        res = s.split(',#1')
        if res[len(res) -1] == '':
            res.pop()
        return res