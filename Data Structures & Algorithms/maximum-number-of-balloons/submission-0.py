class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        arr = [0] * 26
        for char in text:
            arr[ord(char)-ord('a')] += 1
        print(arr)
        b = arr[1]
        a = arr[0]
        l = arr[11] // 2
        o = arr[14] // 2
        n = arr[13] 
        print(b,a,l,o,n)
        return min([b,a,l,o,n])