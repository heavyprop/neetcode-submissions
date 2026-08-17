class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for char in s:
            if char.isalnum():
                new += char
        s = new

        for x in range(len(s)):
            if s[x] != s[len(s) - 1 - x]:
                return False
    

        return True
        