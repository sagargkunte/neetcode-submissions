class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = dict()

        for i in range(len(nums)):
            key = target-nums[i]
            if key in map_:
                return [map_.get(key),i]
            map_[nums[i]] = i
        return [-1,-1]
