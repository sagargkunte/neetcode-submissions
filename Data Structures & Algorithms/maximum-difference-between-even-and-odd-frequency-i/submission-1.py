class Solution:
    def maxDifference(self, s: str) -> int:
        max_oddFreq = 1
        min_evenFreq = 9999
        map_ = defaultdict(int)
        for i in range(len(s)):
            map_[s[i]] += 1
        
        for i in map_.values():
            if i % 2 ==0:
                min_evenFreq = min(i,min_evenFreq)
            else:
                max_oddFreq = max(i,max_oddFreq)
                
        return max_oddFreq-min_evenFreq