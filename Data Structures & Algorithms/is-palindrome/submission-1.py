class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = "".join(ch for ch in s if ch.isalnum())

        left, right = 0, len(st)-1

        while left < right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1
        
        return True

            