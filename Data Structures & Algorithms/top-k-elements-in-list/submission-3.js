class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = {}
        for(let i=0;i<nums.length;i++) {
            map[nums[i]] = (map[nums[i]] || 0) + 1
        }
        console.log(map)
        let heap = new MinPriorityQueue((x) => x[1]);

        for(let [num,count] of Object.entries(map)) {
            heap.enqueue([num,count])

            if(heap.size() > k) heap.dequeue()
        }

        const res = []

        for(let i=0;i<k;i++) {
            const [num,count] = heap.dequeue()
            res.push(num)
        }
        return res
    }
}
