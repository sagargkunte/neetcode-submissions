class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map_ = defaultdict(int)
        max_ = -1
        for ele in arr:
            map_[ele] += 1
        for key,value in map_.items():
            if key == value:
                max_ = max(key,max_)
        return max_
        