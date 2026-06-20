class Solution:
    def isPolindrome(self,left,right):
        while left < right:
            if self.s[left] != self.s[right]:
                return False
            left += 1
            right -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        self.s = s

        left ,right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isPolindrome(left+1,right) or self.isPolindrome(left,right-1)
            left += 1
            right -= 1
        return True
        
        