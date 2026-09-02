class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []

        for s in strs:
            app = f"{len(s)}{"$"}"
            new = f"{app}{s}"
            ret.append(new)
        
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        ret = []
        newstart = 0

        for i in range(len(s)):
            if i < newstart:
                continue
            
            if s[i] == "$":
                # Substring from newstart to i
                # Can't just do the number before i since there can be strings of length 
                # greater than 9.
                length = int(s[newstart:i])
                # At this point i is right before start of string, so we need to add 1 
                # in addition to length to get the newstart. Same logic for string.
                newstart = i + 1 + length
                string = s[i + 1:i + 1 + length]

                ret.append(string)
        
        return ret
