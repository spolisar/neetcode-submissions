class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        for n, count in counts.items():
            freqs[count].append(n)
        result = []
        for i in range(len(freqs) - 1, 0, -1):
            result.extend(freqs[i])
            if len(result) >= k:
                return result