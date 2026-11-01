class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())

        sp = list(s)
        rev = sp.copy()
        rev.reverse()

        return sp == rev
