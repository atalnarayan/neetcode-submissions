class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s))+'#'+s for s in strs])

    def decode(self, s: str) -> List[str]:
        arr, i = list(), 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            arr.append(s[j+1:j+1+length])
            i = j + length + 1
        return arr
