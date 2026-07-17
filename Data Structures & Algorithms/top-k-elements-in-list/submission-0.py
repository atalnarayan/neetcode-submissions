class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freqs = [[] for _ in range(len(nums)+1)]
        for key,val in counter.items():
            freqs[val].append(key)
        
        out = list()
        for freq in freqs[::-1]:
            out.extend(freq)
            if len(out) >= k:
                break
        
        return out[:k]