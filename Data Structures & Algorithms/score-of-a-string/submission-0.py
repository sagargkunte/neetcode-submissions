class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_ = 0
        for i in range(1,len(s)): 
            sum_ += abs(ord(s[i]) - ord(s[i-1]))
        return sum_
