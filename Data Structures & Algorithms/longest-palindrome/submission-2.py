class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)

        res = 0
        for char in s:
            count[char] += 1
            if count[char] %2 == 0:
                res += 2
        if res < len(s):
            return res + 1
        return res
            
        
