class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s))+'#'+s for s in strs)

    def decode(self, s: str) -> List[str]:
        def is_number(string):
            try:
                float(string)
                return True
            except ValueError:
                return False
        arr = []
        start, end = 0, 0
        while end < len(s):
            if is_number(s[end]):
                end+= 1
            else:
                count = int(s[start:end])
                end += 1 # for hash
                arr.append(s[end:end+count])
                start, end = end+count, end + count
        
        return arr

            
