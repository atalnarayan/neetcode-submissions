class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            counter = [0]*26
            for char in word:
                counter[ord(char)-ord('a')] += 1
            anagram_map[tuple(counter)].append(word)
        return list(anagram_map.values())