class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        map_ = dict()
        for char in s:
            map_[char] = map_.get(char,0) + 1
        
        for char in t:
            if not map_.get(char): return False
            map_[char] = map_.get(char) - 1
        
        for ele in map_.values():
            if ele != 0: return False
        return True