class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_ele = set(nums)
        for num in nums:
            length = 1
            if not num-1 in set_ele:
                while num+length in set_ele:
                    length += 1
                longest = max(length,longest)
        return longest