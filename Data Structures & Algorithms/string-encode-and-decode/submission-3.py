class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = []

        for s in strs:
            app = f"{len(s)}{'#'}"
            new = f"{app}{s}"
            ret.append(new)
        
        return "".join(ret)
            

    def decode(self, s: str) -> List[str]:
        ret = []

        start = 0

        for i in range(len(s)):
            if i < start:
                continue
                
            if s[i] == '#':
                leng = int(s[start:i])
                substr = s[i+1:i+1+leng]
                ret.append(substr)

                start = i + 1 + leng
        
        return ret
