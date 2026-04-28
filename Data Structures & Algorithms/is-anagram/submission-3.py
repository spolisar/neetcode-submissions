class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = {}
        t_counts = {}
        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]
            if c_s not in s_counts:
                s_counts[c_s] = 0
            if c_t not in t_counts:
                t_counts[c_t] = 0
            s_counts[c_s] += 1
            t_counts[c_t] += 1
        return s_counts == t_counts