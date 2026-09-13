class Solution:
    def minWindow(self, s: str, t: str) -> str:
        occurences = Counter(t)
        check = Counter()
        have, need = 0, len(occurences)
        res, res_len = (-1, -1), float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            check[c] += 1
            if c in occurences and check[c] == occurences[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = (l, r)
                    res_len = r - l + 1
                check[s[l]] -= 1
                if s[l] in occurences and check[s[l]] < occurences[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""