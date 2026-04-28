class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            counts = [0 for _ in range(26)]
            for c in s:
                c_val = ord(c) - ord('a')
                counts[c_val] += 1
            group_key = tuple(counts)
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(s)
        return [groups[k] for k in groups.keys()]
