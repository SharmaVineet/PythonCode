import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for i in s.lower():
            if i not in string.whitespace and i not in string.punctuation:
                n += i
        if n == n[::-1]:
            return True
        return False


p = Solution()
print(p.isPalindrome("A man, a plan, a canal: Panama"))
