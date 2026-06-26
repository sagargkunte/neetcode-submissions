class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()
        left = 0
        max_count = 0
        for right in range(len(s)):
            while s[right] in set_:
                set_.remove(s[left])
                left += 1
            set_.add(s[right])
            max_count = max(max_count,right-left+1)
        return max_count