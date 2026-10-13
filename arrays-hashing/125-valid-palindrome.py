# Time Complexity: O(n)
# Space complexity: O(k) -> k is size of string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalnum()])
        return s == s[::-1]
        
