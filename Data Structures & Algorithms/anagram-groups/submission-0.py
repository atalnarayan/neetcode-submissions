class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            anagram_map["".join(sorted(s))].append(s)
        
        return list(anagram_map.values())