class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const map = new Map();
        for(let i=0;i<nums.length;i++) {
            map.set(nums[i],(map.get(nums[i]) || 0) + 1)
        }
        console.log(map)
        for(let [key,value] of map) {
            if(value > 1) {
                return true;
            }
        }
        return false;
    }
}
