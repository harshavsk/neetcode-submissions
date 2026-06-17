class Solution:

    def encode(self, strs: List[str]) -> str:
        res =[]
        for s in strs:
            res.append(str(len(s)))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        sizes = []
        res = []
        i = 0
        while i<len(s) and s[i]!='#':
            temp = ''
            while s[i]!=',':
                temp = temp+s[i]
                i+=1
            sizes.append(int(temp))
            i+=1
        i+=1
        for size in sizes:
            res.append(s[i:i+size])
            i+=size
        return res
