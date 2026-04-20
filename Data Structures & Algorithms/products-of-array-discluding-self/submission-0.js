class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let n = nums.length;
        let res = new Array()
        let prefix = new Array()
        let suffix = new Array()
        prefix[0] = 1;
        suffix[n-1] = 1;

        for(let i=1;i<n;i++) {
            prefix[i] = nums[i-1] * prefix[i-1]
        }
        console.log(prefix)
        for(let i=n-2;i>=0;i--) {
            suffix[i] = nums[i+1] * suffix[i+1]
        }
        console.log(suffix)
        for(let i =0;i<n;i++) {
            res[i] = prefix[i] * suffix[i]
        }
        console.log(res)
        return res

    }
}
