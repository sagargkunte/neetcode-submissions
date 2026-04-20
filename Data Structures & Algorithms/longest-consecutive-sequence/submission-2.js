class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums)
        let long = 0;
        for(let num of numSet) {
            if(!numSet.has(num-1)) {
                let length = 1;
                while(numSet.has(num+length)) {
                    length++;
                }
                long = Math.max(long,length)
            }
        }
        return long
    }
}
