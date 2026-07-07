class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        set_ = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in set_:
                res.add(nums1[i])
        return list(res)