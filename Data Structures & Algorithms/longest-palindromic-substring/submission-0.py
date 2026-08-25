class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def expand(l: int, r: int):
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)       # odd length, centered at i
            expand(i, i + 1)   # even length, centered between i and i+1

        return res