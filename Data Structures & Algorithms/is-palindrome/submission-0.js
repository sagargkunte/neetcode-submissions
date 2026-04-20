class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let first = 0,last = s.length-1;
        const alpha = new Set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789");
        while(first < last) {
            if(!alpha.has(s[first])) {
                first++
            } else if(!alpha.has(s[last])) {
                last--
            } else {
                if(!(s[first].toLowerCase()==s[last].toLowerCase())) {
                    return false;
                }
                first++
                last--
            }
        }
        return true
    }
}
