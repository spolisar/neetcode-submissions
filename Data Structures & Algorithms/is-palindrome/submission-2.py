class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for c in s:
            if c.isalnum():
                word += c
        word = word.lower()
        return word == word[::-1]