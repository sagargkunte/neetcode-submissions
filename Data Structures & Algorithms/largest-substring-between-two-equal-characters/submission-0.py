class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        map_ = dict()
        max_subset = -1
        for i,char in enumerate(s):
            if char in map_:
                max_subset = max(max_subset,i-map_[char]-1)
            else:
                map_[char] = i
        
        return max_subset