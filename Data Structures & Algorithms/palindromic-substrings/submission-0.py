class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            res += self.countPalindrome(s, l, r)

            # Even length palindromes
            l, r = i, i + 1
            res += self.countPalindrome(s, l, r)
            
        return res

    def countPalindrome(self, s, l, r):
        res = 0
        while l >=0 and r < len(s) and s[l]==s[r]:
                res += 1
                l -= 1
                r += 1
        return res
        