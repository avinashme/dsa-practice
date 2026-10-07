class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for c in s:
            s_count[c] = s_count.get(c, 0) + 1

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        return s_count == t_count
