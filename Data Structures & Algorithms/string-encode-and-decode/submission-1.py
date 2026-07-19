class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s))+'#'+s for s in strs)

    def decode(self, s: str) -> List[str]:
        arr = []
        start, end = 0, 0
        while end < len(s):
            if (s[end]).isdigit():
                end+= 1
            else:
                count = int(s[start:end])
                end += 1 # for hash
                arr.append(s[end:end+count])
                start, end = end+count, end + count
        
        return arr

            
