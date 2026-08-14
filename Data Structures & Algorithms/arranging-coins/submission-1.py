class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        curr = 0
        while n >= count:
            n = n - count
            count = count + 1
        return count-1
