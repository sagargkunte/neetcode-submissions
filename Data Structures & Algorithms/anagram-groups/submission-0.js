class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let obj = new Object();
        for(let s of strs) {
            let arr = new Array(26).fill(0)
            for(let i=0;i<s.length;i++) {
                arr[s.charCodeAt(i)-'a'.charCodeAt(0)]++;
            }
            let key = arr.join(',')
            if(!obj[key]) {
                obj[key] = []
            }
            obj[key].push(s)
        }
        console.log(obj)
        return Object.values(obj)
    
    }
}
