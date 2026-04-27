class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0,right = heights.length-1;
        let max = 0;
        while(left < right) {
           let [length,bredth] = [Math.min(heights[left],heights[right]),right-left]
           let area = length * bredth;
           max = Math.max(max,area)
           if(heights[left] > heights[right]) {
                right--
           } else {
                left++
           }
        }
        return max
    }
}
