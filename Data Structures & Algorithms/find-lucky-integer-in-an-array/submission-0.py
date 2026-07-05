class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map_ = defaultdict(int)
        max_ele = -1
        for i in range(len(arr)):
            map_[arr[i]] += 1
        
        for key,value in map_.items():
            if key == value:
                max_ele = max(max_ele,value)
            
        return max_ele