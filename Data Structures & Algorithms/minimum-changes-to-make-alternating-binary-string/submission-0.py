class Solution:
    def minOperations(self, s: str) -> int:
        curr = 1
        count1 = 0
        for char in s:
            if int(char) != curr:
                count1 += 1
            curr = curr ^ 1
        
        curr = 0
        count2 = 0
        for char in s:
            if int(char) != curr:
                count2 += 1
            curr = curr ^ 1
        print(count1,count2)
        return min(count1,count2)
