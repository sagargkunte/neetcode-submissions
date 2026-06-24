class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # alpha = [1] * 27
        # # print(alpha)
        n = columnNumber
        # for i in range(1,27):
        #     alpha[i] += i
        # print(alpha)
        s = ""
        while n:
            n-= 1
            rem = n % 26
            s = chr(65+rem) + s 
            n = n // 26
        return s