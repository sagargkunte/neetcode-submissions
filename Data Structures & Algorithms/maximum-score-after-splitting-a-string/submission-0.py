class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        i = 1
        while i < len(s):
            left = s[0:i]
            right = s[i:]
            zero = left.count("0")
            one = right.count("1")
            res = max(zero+one,res)
            i += 1
        return res