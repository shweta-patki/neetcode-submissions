class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sfreq = sorted(freq, key=freq.get, reverse=True)
        print(sfreq)
        return sfreq[:k]