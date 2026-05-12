class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for str in strs:
            freq = [0] * 26

            for ch in str:
                freq[ord(ch) - ord('a')] += 1

            freq = tuple(freq)
            if freq in d:
                d[freq].append(str)
            else:
                d[freq] = [str]
        
        return list(d.values())