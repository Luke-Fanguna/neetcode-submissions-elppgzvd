class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        def expand(l, r):
            found_palindromes = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                found_palindromes += 1
                l -= 1
                r += 1
            return found_palindromes
        other = 0
        for i in range(len(s)):
            palindromes += expand(i, i)
            palindromes += expand(i, i+1)
        # print(other)
        return palindromes